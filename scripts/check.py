#!/usr/bin/env python3
"""Offline checks for AIBoot's source format, not for agent behavior.

Only simple Markdown/HTML local links and source-file structure are supported.
This is intentionally not a general Markdown parser.
"""

import os
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
IGNORED_DIRS = {".git", ".venv", "__pycache__", ".cache", "tmp"}


def markdown_files(root):
    for directory, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in IGNORED_DIRS)
        for name in sorted(files):
            if name.endswith(".md"):
                yield Path(directory) / name


def source_files(root):
    """Use Git's file set so ignored local notes cannot mask packaging errors."""
    if not (root / ".git").exists():
        return None  # A Git-host ZIP already contains only the distributed files.
    result = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        capture_output=True, text=True, check=True,
    )
    return {(root / name).resolve() for name in result.stdout.split("\0") if name}


def prose_lines(text):
    """Ignore fenced examples while retaining line numbers for diagnostics."""
    marker = None
    for number, line in enumerate(text.splitlines(), 1):
        fence = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if marker is None:
                marker = fence.group(1)
            elif fence.group(1)[0] == marker[0] and len(fence.group(1)) >= len(marker) and not fence.group(2).strip():
                marker = None
            yield number, ""
        else:
            yield number, line if marker is None else ""
    if marker is not None:
        raise ValueError("unclosed fenced code block")


def heading_ids(text):
    counts = {}
    result = set()
    for _, line in prose_lines(text):
        heading = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not heading:
            continue
        raw = re.sub(r"<[^>]*>", "", heading.group(1)).lower()
        slug = re.sub(r"[^\w\-\s]", "", raw).replace(" ", "-")
        number = counts.get(slug, 0)
        counts[slug] = number + 1
        result.add(slug if number == 0 else f"{slug}-{number}")
    return result


def check_links(path, text, root, sources=None):
    errors = []
    try:
        lines = list(prose_lines(text))
    except ValueError as exc:
        return [str(exc)]
    for number, line in lines:
        line = re.sub(r"`[^`]*`", "", line)
        targets = re.findall(r"!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+\"[^\"]*\")?\s*\)", line)
        targets += re.findall(r"(?:href|src)=[\"']([^\"']+)[\"']", line)
        definition = re.match(r"^\s{0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)", line)
        if definition:
            targets.append(definition.group(1))
        for raw in targets:
            url = urlsplit(raw.strip("<>"))
            if url.scheme or url.netloc:
                continue
            target = (path.parent / unquote(url.path)).resolve() if url.path else path.resolve()
            if not target.is_relative_to(root.resolve()):
                errors.append(f"line {number}: local link escapes the repository: {raw}")
            elif not target.exists():
                errors.append(f"line {number}: missing local target: {raw}")
            elif sources is not None and target.is_file() and target not in sources:
                errors.append(f"line {number}: local target is excluded from the source kit: {raw}")
            elif url.fragment and target.suffix == ".md":
                try:
                    anchors = heading_ids(target.read_text(encoding="utf-8"))
                    if unquote(url.fragment) not in anchors:
                        errors.append(f"line {number}: missing heading: {raw}")
                except (UnicodeError, ValueError) as exc:
                    errors.append(f"line {number}: invalid Markdown target {raw}: {exc}")
    return errors


def check_repository(root):
    errors = []
    sources = source_files(root)
    paths = [path for path in markdown_files(root) if sources is None or path.resolve() in sources]
    for path in paths:
        relative = path.relative_to(root)
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{relative}: cannot read UTF-8: {exc}")
            continue
        findings = check_links(path, text, root, sources)
        if not text.endswith("\n"):
            findings.append("missing final newline")
        errors.extend(f"{relative}: {finding}" for finding in findings)
    if not (root / "scaffold/AGENTS.md").is_file():
        errors.append("missing distributable scaffold/AGENTS.md")
    return errors, len(paths)


def main():
    errors, documents = check_repository(ROOT)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"Checked {documents} Markdown files: source checks passed.")
    print("Native loading, agent behavior, and token savings are not assessed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
