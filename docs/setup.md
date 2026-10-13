# Add AIBoot to a project

[English overview](../README.md) · [中文概览](../README.zh-CN.md)

The kit is `v0.2.0-alpha.5`: one default English core, loaded by your coding tool.
Existing project conventions, native plans, checks, and appropriate installed
Skills continue to supply the rest of the workflow.

## Inspect and add the core

Get a local copy using your Git host's clone or Download ZIP action. Run this
POSIX-shell example in the destination project on macOS/Linux. On Windows, copy
the same file using your file manager or editor.

Check existing instructions before copying. For a destination without `AGENTS.md`:

```sh
AIBOOT_SOURCE="/absolute/path/to/AIBoot"
test ! -e AGENTS.md && test ! -L AGENTS.md && \
  cp "$AIBOOT_SOURCE/scaffold/AGENTS.md" AGENTS.md
```

The guard exits nonzero and leaves an existing file or symlink untouched. If one
exists, review the source and merge useful guidance in your editor. Preserve local
conventions and an identifiable AIBoot section with its source version.

Follow one guide for the tool's actual loading behavior:

- [Codex](../adapters/codex/README.md).
- [Cursor](../adapters/cursor/README.md).
- [Claude Code](../adapters/claude-code/README.md).

## Check the addition

Inspect the tool's effective instructions where available; start a fresh session
if discovery has not refreshed. Confirm loading separately from useful behavior.
A filename repeated by the agent does not prove either. Try a relevant project
task and an ordinary edit that should proceed directly.

Record the source version or commit in the normal Git change description.
Keep facts in existing project documents; save missing facts only when future work
would otherwise lose them. No prescribed facts template or extra task ledger is
needed. When redistributing AIBoot content, retain its MIT notice in existing
third-party notices or a copy of [LICENSE](../LICENSE), preserving your own license.

## Continue work across sessions

The core includes continuity guidance. Use native recovery and existing durable
plans, issues, or project documents when they contain enough information to
continue. If future sessions or collaborators would otherwise lose necessary
state and no suitable entry exists, keep one short status note in the project's
normal document location. There is no required filename or document bundle.

Keep the current goal, verified results and evidence links, unfinished work,
blockers, next action, and consequential constraints or decision references.
Update the affected facts at a milestone, material goal change, blocker, or
handoff. Routine edits can rely on existing task records and Git changes.

At resumption, read the relevant state and inspect the actual Git/worktree and
applicable evidence. Correct stale status; distinguish implemented work from
verified completion. Repeat checks when their evidence no longer applies.

Build coding and testing conventions from existing stack configuration and team
agreements. Put missing agreed conventions in existing project guidance; add
architecture or decision documents when future work needs their explanation.
Version shared records according to the destination project's policies.

AIBoot's own ignored maintenance documents and scripts belong to this repository.
The setup copies the core, not AIBoot's `.gitignore`. Your project's shared plans,
conventions, and decisions follow its own collaboration and versioning needs.

## Optional capability discovery

The core includes task triggers, direct public discovery sources, and failure
guidance. Describe the actual work; it can match suitable installed capabilities
without a Skill name in the task. New specialized needs can justify discovery;
ordinary edits and restarts do not require it. The default setup needs only the core.

For curated detail, give the agent access to
[the capability reference](../scaffold/capabilities.md) when needed, using a file
attachment or its actual local source path. It contains selection guidance and
ten task-specific routes, including MCP/private integrations and failure paths,
not installed Skills or tools.

To retain the reference in a destination project, inspect its existing document
layout and copy it manually, or use this guarded POSIX-shell example:

```sh
AIBOOT_SOURCE="/absolute/path/to/AIBoot"
test ! -e docs/aiboot-capabilities.md && test ! -L docs/aiboot-capabilities.md && \
  mkdir -p docs && \
  cp "$AIBOOT_SOURCE/scaffold/capabilities.md" docs/aiboot-capabilities.md
```

If useful, add this pointer to the project's native instruction entry in your
editor, adjusting the path to the actual location:

```text
When a task needs a specialized capability or existing methods leave a useful gap,
consult the selection guidance and matching section of docs/aiboot-capabilities.md.
Read it on demand; do not import it into always-loaded context. Execution stays native.
```

Use a plain pointer, not a Claude `@` import, duplicate always-on rule, or skill
wrapper. With the core alone, agents can still use installed capabilities and
discover upstream sources; the curated file is optional. A copied reference uses
external links and remains independent of the original AIBoot checkout.

Choose one relevant upstream capability through the host's native mechanism within
existing authorization. Inspect its current workflow, license, dependencies, and
setup effects first. Check selected access through actual task use; a directory
entry alone proves neither connection nor authorization. Use official docs or
existing methods when sufficient; report essential access that remains unavailable.
This setup does not install packages, connect services, or enable hooks. Keep
additions in normal project Git changes; no extra capability inventory is required.

## Update and remove

Compare the previous source, new source, and local copy using the recorded version.
Review and apply relevant changes manually, preserving user edits. Commit the
reviewed delta and record the new version in the existing change description.

To remove AIBoot, review the original addition and subsequent edits. Remove only
identifiable AIBoot guidance, an import, or an optional reference pointer added for
it. Keep project facts, local conventions, user modifications, and required notices
for content retained.
A formerly AIBoot-owned file with useful project content needs editing, not
automatic deletion.

Review an optional copied reference through the same update process. Remove only
its AIBoot-owned content when it is no longer useful. Third-party installations
are independent additions; removing this reference does not uninstall them.

Recheck changed loading paths and affected behavior. Use a fresh session and the
project's normal checks as relevant; unrelated edits do not require every case to
be rerun. No application code or runtime import depends on AIBoot.

## Migrate from the first alpha

This version folds startup into the core and no longer distributes
`aiboot-start`, `aiboot-select`, or the project facts template.

Review any installed copies of those two Skills before removing them; preserve
useful local changes. Remove obsolete calls or references from your own guidance.
Keep project facts you have already written. Apply the new core through the same
reviewed update process, then describe a real task directly to your tool.

The source checker validates this repository's files and copy guard. Native agent
behavior, cross-tool coexistence, and remote/cloud use have separate evidence
requirements; they are not established by a successful file copy.
