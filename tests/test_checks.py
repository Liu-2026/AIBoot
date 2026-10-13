import importlib.util
import os
import re
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("aiboot_check", ROOT / "scripts/check.py")
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


class ContentChecks(unittest.TestCase):
    @unittest.skipUnless(shutil.which("git"), "Git source membership needs Git")
    def test_ignored_notes_do_not_hide_a_broken_public_link(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            subprocess.run(["git", "init", "--quiet", str(root)], check=True)
            (root / ".gitignore").write_text("/internal.md\n", encoding="utf-8")
            (root / "internal.md").write_text("[private example](absent.md)\n", encoding="utf-8")
            (root / "scaffold").mkdir()
            (root / "scaffold/AGENTS.md").write_text("# Guidance\n", encoding="utf-8")
            page = root / "README.md"
            page.write_text("# Public\n", encoding="utf-8")
            findings, documents = CHECK.check_repository(root)
            self.assertEqual(findings, [])
            self.assertEqual(documents, 2)
            page.write_text("[private](internal.md)\n", encoding="utf-8")
            findings, _ = CHECK.check_repository(root)
            self.assertEqual(len(findings), 1)
            self.assertIn("excluded from the source kit", findings[0])

    def test_missing_target_and_heading_are_reported(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            page = root / "README.md"
            page.write_text("# Guide\n", encoding="utf-8")
            findings = CHECK.check_links(page, "[file](missing.md)\n[section](#absent)\n", root)
            self.assertEqual(len(findings), 2)
            self.assertIn("missing local target", findings[0])
            self.assertIn("missing heading", findings[1])

    def test_examples_are_ignored_but_html_assets_are_checked(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            page = root / "README.md"
            content = '```md\n[example](missing.md)\n```\n<img src="missing.png">\n'
            findings = CHECK.check_links(page, content, root)
            self.assertEqual(len(findings), 1)
            self.assertIn("missing.png", findings[0])

    def test_unclosed_fences_and_nonportable_links_fail(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            page = root / "README.md"
            self.assertIn("unclosed", CHECK.check_links(page, "```\n", root)[0])
            self.assertIn("escapes", CHECK.check_links(page, "[outside](../other.md)\n", root)[0])


@unittest.skipUnless(os.name == "posix", "documented shell copy examples are POSIX-only")
class DocumentedCopyGuards(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        text = (ROOT / "docs/setup.md").read_text(encoding="utf-8")
        blocks = re.findall(r"```sh\n(.*?)\n```", text, re.DOTALL)
        # Exercise the actual documented commands; supply the source via env.
        cls.core_command = "\n".join(blocks[0].splitlines()[1:])

    def run_copy(self, command, root):
        env = os.environ.copy()
        env["AIBOOT_SOURCE"] = str(ROOT)
        return subprocess.run(["sh", "-c", command], cwd=root, env=env, capture_output=True)

    def test_clean_destination_receives_the_source_files(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.assertEqual(self.run_copy(self.core_command, root).returncode, 0)
            self.assertEqual((root / "AGENTS.md").read_bytes(), (ROOT / "scaffold/AGENTS.md").read_bytes())

    def test_existing_core_is_preserved(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "AGENTS.md").write_text("User instructions\n", encoding="utf-8")
            self.assertNotEqual(self.run_copy(self.core_command, root).returncode, 0)
            self.assertEqual((root / "AGENTS.md").read_text(), "User instructions\n")

    def test_dangling_symlink_is_not_followed_or_replaced(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            target = root / "absent.md"
            (root / "AGENTS.md").symlink_to(target)
            self.assertNotEqual(self.run_copy(self.core_command, root).returncode, 0)
            self.assertTrue((root / "AGENTS.md").is_symlink())
            self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()
