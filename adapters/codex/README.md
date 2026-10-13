# Codex: core loading

Use [the shared setup](../../docs/setup.md) for copying, merging, updates, and removal.

Codex discovers project guidance from the project root toward the current working
directory, with more local guidance taking precedence. At each level,
`AGENTS.override.md` takes precedence over `AGENTS.md`. Check the effective chain
when the core does not appear; preserve existing overrides and user guidance.

Launch a fresh session in the destination project after updating instructions.
Describe the task directly. Plans, tools, session recovery, and permitted subagents
remain native Codex capabilities.

Status: official documentation checked on 2026-10-13. Local Codex CLI
`0.162.0-alpha.17.2` input previews confirmed the complete core appears once after
copying and is absent before copying and after removal. These previews did not run
a model; remote/cloud support and broader behavior have separate validation scopes.

Source: [Codex project instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
