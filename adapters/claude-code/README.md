# Claude Code: core loading

Use [the shared setup](../../docs/setup.md) for copying, merging, updates, and removal.

Direct `AGENTS.md` loading requires Claude Code v2.1.277 or later and an eligible
session. Under the documented default, a `CLAUDE.md`, `.claude/CLAUDE.md`, or
`CLAUDE.local.md` in the working directory or an ancestor takes precedence.
Check the actual version, Project instructions setting, and effective files.

When direct loading is unavailable, or your existing Claude guidance is the entry,
add this project-local import to `CLAUDE.md` while preserving its contents:

```text
@AGENTS.md
```

The path is relative to the importing file. Inspect the next session's `/context`
and loaded memory files rather than assuming a filename establishes loading.
Use the existing project entry; global settings need no change.

Describe the task directly. Planning, installed Skills, session recovery, and
permitted subagents remain native Claude Code capabilities.

Status: official documentation checked on 2026-10-13; native loading and behavior
have not been tested by AIBoot. Remote/cloud behavior is outside the verified scope.

Source: [Claude Code project instructions](https://code.claude.com/docs/en/memory).
