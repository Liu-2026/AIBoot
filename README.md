<p align="center">
  <img src="docs/assets/aiboot-hero.png" alt="AIBoot — Build the right thing. Keep it lean." width="100%">
</p>

<p align="center">
  <strong>Give your AI coding agent an engineering mindset.</strong><br>
  Clear direction · Smart reuse · Focused delivery
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-2f855a" alt="MIT License"></a>
  <a href="docs/setup.md"><img src="https://img.shields.io/badge/version-v0.2.0--alpha.4-2563eb" alt="v0.2.0-alpha.4"></a>
</p>

<p align="center">
  <strong>English</strong> · <a href="README.zh-CN.md">简体中文</a><br>
  <a href="#quick-start">Quick start</a> · <a href="#the-right-capability-for-the-task">Skills & tools</a> · <a href="docs/setup.md">Setup guide</a> · <a href="CONTRIBUTING.md">Contribute</a>
</p>

---

# AIBoot

**From a clear idea to a thoughtfully built project.**

AIBoot brings practical engineering guidance to **Codex, Cursor, and Claude Code**.
It helps your agent clarify the goal, choose proven building blocks, plan the next
useful step, and deliver with relevant verification.

**One core file. Your favorite tools. Your own stack.** Add AIBoot to your project's
native instruction entry and describe what you want to build. Its English guidance
works with your coding tool's plans, Skills, MCP integrations, session recovery,
and permitted subagents.

## Why AIBoot

Good projects begin with good decisions. AIBoot puts those decisions within reach
of your AI coding workflow:

- **A clear starting point.** Turn an idea into a concrete goal, a sensible first
  milestone, and actionable development work.
- **An instinct for reuse.** Consider mature libraries, existing applications,
  official starters, and specialized capabilities before choosing an implementation.
- **Architecture that fits.** Shape frontend, backend, data, deployment, and quality
  work around the project's users and actual needs.
- **The right capability at the right time.** Match design, documentation,
  integrations, and specialist tasks to suitable native Skills and tools.
- **Context with purpose.** Read specialized references on demand and keep the
  project facts that help future decisions and handoffs.
- **A clear finish.** Verify the relevant result and give the user an accurate,
  useful account of what was delivered.

Use it to guide a personal script, a company tool, a customer product, or the next
project you are starting from scratch.

## Quick start

### 1. Get AIBoot

Clone with `git clone https://github.com/Liu-2026/AIBoot.git`, or
[download the ZIP](https://github.com/Liu-2026/AIBoot/archive/refs/heads/main.zip).

### 2. Add the core

In your destination project, run:

```sh
AIBOOT_SOURCE="/absolute/path/to/AIBoot"
test ! -e AGENTS.md && test ! -L AGENTS.md && \
  cp "$AIBOOT_SOURCE/scaffold/AGENTS.md" AGENTS.md
```

The macOS/Linux command preserves existing files and symlinks. If your project
already has instructions, merge the useful guidance in your editor. On Windows,
copy the same file manually. See the [setup guide](docs/setup.md) for details.

Choose your tool's loading guide:

- **[Codex](adapters/codex/README.md)** — project `AGENTS.md`.
- **[Cursor](adapters/cursor/README.md)** — project `AGENTS.md`.
- **[Claude Code](adapters/claude-code/README.md)** — direct `AGENTS.md` loading where
  supported, or a project-local `CLAUDE.md` import.

### 3. Describe the outcome

```text
Build a small booking app for our team.
Start with the simplest useful booking flow.
Consider suitable existing libraries and native Skills or tools.
Implement the first working result and show how you verified it.
```

For research and planning, add “plan only; do not implement yet.” To continue an
existing project, describe the next result and point to the current project facts.

## The right capability for the task

**Describe the work. Let the guidance help your agent find the right approach.**

The default core includes task triggers and discovery sources. At project start,
a material task change, or a specialized need, it guides the agent to consider
appropriate installed Skills, connected tools, and existing project methods.

- **Interface design:** an appropriate design Skill, such as Impeccable, can help
  shape a distinctive visual direction around your product and its users.
- **SDK and API work:** a connected Context7 tool or official versioned docs can
  provide relevant implementation references.
- **External services:** existing integrations and native plugin/MCP discovery
  can connect the task to the right service capability.
- **Everyday changes:** focused implementation and relevant checks keep small
  edits straightforward.

When a useful gap remains, upstream projects, skills.sh, and public MCP metadata
provide discovery candidates. Organization sources guide private integrations.
Your coding tool handles loading, authorization, and execution.

The optional [capability reference](scaffold/capabilities.md) provides **ten focused
routes** across documentation, UI, React, browser verification, Postgres, mobile,
Azure SDKs, security review, document artifacts, and service integrations.
[Add it when useful](docs/setup.md#optional-capability-discovery) and read the relevant
section on demand.

## Built for the way you work

- **Starting a new app:** clarify the first useful flow and select a fitting stack.
- **Building an internal tool:** explore suitable existing products and libraries.
- **Creating a branded page:** connect real content and references to a design Skill.
- **Making a small change:** keep implementation and verification focused on the task.
- **Resuming a project:** continue from current facts and applicable evidence.
- **Preparing for maintenance:** favor readable code, clear boundaries, and useful
  project knowledge as the application evolves.

## Small core, broad reach

```text
scaffold/AGENTS.md            # core engineering guidance
scaffold/capabilities.md      # optional task-specific capability reference
adapters/                    # native loading guides for each tool
docs/setup.md                # setup, migration, updates, and removal
docs/assets/aiboot-hero.png   # project artwork
```

AIBoot stays in the instruction layer. Your project keeps its technical stack,
application layout, tests, CI, and existing documentation. Native tools provide
execution; the core supplies a shared engineering approach.

## Build with us

AIBoot is **open source under MIT**. Bring your workflow, share a practical use
case, improve a capability route, or help make the guidance clearer.

- [Contributing](CONTRIBUTING.md) — Git workflow and contribution guidance.
- [Setup guide](docs/setup.md) — installation and project lifecycle.
- [Issues](https://github.com/Liu-2026/AIBoot/issues) — ideas, feedback, and useful examples.

**Like the approach? Give AIBoot a Star and help more developers build with intent.**

## License

[MIT](LICENSE). Project artwork was created for AIBoot.
