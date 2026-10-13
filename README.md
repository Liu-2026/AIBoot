<p align="center">
  <img src="docs/assets/aiboot-hero.png" alt="AIBoot — Build the right thing. Keep it lean." width="100%">
</p>

<p align="center">
  <strong>Build beyond the first demo.</strong><br>
  Your AI agent’s engineering playbook — from idea to delivery.
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-2f855a" alt="MIT License"></a>
  <a href="docs/setup.md"><img src="https://img.shields.io/badge/version-v0.2.0--alpha.8-2563eb" alt="v0.2.0-alpha.8"></a>
</p>

<p align="center">
  <strong>English</strong> · <a href="README.zh-CN.md">简体中文</a><br>
  <a href="#quick-start">Quick start</a> · <a href="#how-to-use-aiboot">Usage & prompts</a> · <a href="#skills-and-tools-at-the-right-moment">Skills & tools</a> · <a href="CONTRIBUTING.md">Contribute</a>
</p>

---

# AIBoot

**Turn ambitious ideas into thoughtfully engineered software.**

AIBoot brings a shared engineering playbook to **Codex, Cursor, and Claude Code**:
clarify requirements, research proven solutions, choose architecture, plan the
work, build integrated features, and prepare a usable delivery. It gives your
agent guidance for the whole journey, including future sessions and maintenance.

**A shared core. Focused capability routes. Your own stack.** Add the English guidance
to your project's native instruction entry, then describe the outcome you want.
Your coding tool provides execution, planning, Skills, MCP connections, session
recovery, and permitted collaboration. AIBoot connects those capabilities to
practical engineering decisions.

**Great results come first.** Invest in the analysis, design, documentation, and
verification the product needs. Keep architecture and process grounded in actual
users, constraints, and business value.

## Why AIBoot

- **Start with direction.** Turn an idea into a clear scope, observable acceptance,
  and an actionable development plan.
- **Stand on proven foundations.** Consider maintained libraries, existing
  applications, official starters, and specialized capabilities before custom work.
- **Design for your reality.** Shape frontend, backend, data, and deployment around
  the product's actual needs and the team's ability to maintain it.
- **Connect requirements to delivery.** Keep important requirements linked to
  tasks, implementation, and completion evidence in normal project records.
- **Keep momentum.** Carry goals, decisions, verified progress, and the next action
  into the following session or collaborator's work.
- **Bring in the right expertise.** Match interface design, SDK integration,
  specialist artifacts, and external services to relevant native Skills and tools.
- **Build for what comes next.** Address integration, review, usable instructions,
  compatibility, and consequential maintenance needs as the project evolves.

Use it for a personal script, a company tool, a customer product, or a substantial
project with multiple modules and milestones.

## Quick start

### 1. Choose your own project directory

For a new product, create a separate directory and initialize Git when appropriate
with `git init`. For existing software, open its current project root.
AIBoot supplies engineering guidance; the application's structure comes from the
chosen stack, an appropriate starter, and the project's needs.

### 2. Pull the recommended complete kit

**Use AIBoot as a tool in your own project:** pull the core guidance and capability
reference directly. The core includes its path and guides specialized tasks to
read the selection guidance and matching section on demand.

Run one of the following snippets **in your destination project root**. It downloads
only two guidance files plus the MIT notice, without cloning the repository or
installing a runtime, third-party Skills, or MCP services.

<details open>
<summary><strong>macOS / Linux — direct download</strong></summary>

```bash
(
  set -eu
  AIBOOT_REF="main" # Or an exact commit for reproducible setup.
  AIBOOT_BASE="https://raw.githubusercontent.com/Liu-2026/AIBoot/$AIBOOT_REF"
  for AIBOOT_TARGET in AGENTS.md docs/aiboot-capabilities.md docs/aiboot-LICENSE; do
    if [ -e "$AIBOOT_TARGET" ] || [ -L "$AIBOOT_TARGET" ]; then
      printf 'Already exists; merge manually: %s\n' "$AIBOOT_TARGET" >&2
      exit 1
    fi
  done
  AIBOOT_TMP=$(mktemp -d)
  trap 'rm -rf "$AIBOOT_TMP"' 0
  curl -fSL "$AIBOOT_BASE/scaffold/AGENTS.md" -o "$AIBOOT_TMP/AGENTS.md"
  curl -fSL "$AIBOOT_BASE/scaffold/capabilities.md" -o "$AIBOOT_TMP/capabilities.md"
  curl -fSL "$AIBOOT_BASE/LICENSE" -o "$AIBOOT_TMP/LICENSE"
  mkdir -p docs
  (set -C; cat "$AIBOOT_TMP/AGENTS.md" > AGENTS.md)
  (set -C; cat "$AIBOOT_TMP/capabilities.md" > docs/aiboot-capabilities.md)
  (set -C; cat "$AIBOOT_TMP/LICENSE" > docs/aiboot-LICENSE)
)
```

</details>

<details>
<summary><strong>Windows — PowerShell direct download</strong></summary>

```powershell
& {
  $ErrorActionPreference = 'Stop'
  $aibootRef = 'main' # Or an exact commit for reproducible setup.
  $aibootBase = "https://raw.githubusercontent.com/Liu-2026/AIBoot/$aibootRef"
  $aibootFiles = @(
    @{ Source = 'scaffold/AGENTS.md'; Target = 'AGENTS.md' },
    @{ Source = 'scaffold/capabilities.md'; Target = 'docs/aiboot-capabilities.md' },
    @{ Source = 'LICENSE'; Target = 'docs/aiboot-LICENSE' }
  )
  foreach ($aibootFile in $aibootFiles) {
    if (Get-Item -LiteralPath $aibootFile.Target -Force -ErrorAction SilentlyContinue) {
      throw "Already exists; merge manually: $($aibootFile.Target)"
    }
  }
  $aibootTemp = Join-Path ([IO.Path]::GetTempPath()) ([Guid]::NewGuid().ToString())
  New-Item -ItemType Directory -Path $aibootTemp | Out-Null
  try {
    foreach ($aibootFile in $aibootFiles) {
      $aibootStaged = Join-Path $aibootTemp ([IO.Path]::GetFileName($aibootFile.Target))
      Invoke-WebRequest -Uri "$aibootBase/$($aibootFile.Source)" -OutFile $aibootStaged
    }
    New-Item -ItemType Directory -Path 'docs' -Force | Out-Null
    foreach ($aibootFile in $aibootFiles) {
      $aibootStaged = Join-Path $aibootTemp ([IO.Path]::GetFileName($aibootFile.Target))
      [IO.File]::Copy($aibootStaged, [IO.Path]::GetFullPath($aibootFile.Target), $false)
    }
  } finally {
    Remove-Item -LiteralPath $aibootTemp -Recurse -Force
  }
}
```

</details>

Both snippets stage all downloads before copying and preserve existing destination
files. If a destination is occupied, use the manual route below to review and merge.
They do not change your product's Git remote, history, settings, or license.
For a fixed source revision, replace `main` with an exact commit in the snippet.

**Manual download or an existing project:** obtain
[the core](https://raw.githubusercontent.com/Liu-2026/AIBoot/main/scaffold/AGENTS.md),
[the capability reference](https://raw.githubusercontent.com/Liu-2026/AIBoot/main/scaffold/capabilities.md),
and [the MIT notice](https://raw.githubusercontent.com/Liu-2026/AIBoot/main/LICENSE).
Save or merge them at the following paths, preserving existing project conventions:

```text
MyProject/
├── AGENTS.md                    # core guidance + your project conventions
├── docs/
│   ├── aiboot-capabilities.md    # task-specific routes, read on demand
│   └── aiboot-LICENSE            # MIT notice for the copied AIBoot content
└── ...                          # your application and its own Git history
```

The core already routes specialized tasks to `docs/aiboot-capabilities.md`.
If you choose a different location or merge into an older instruction entry, add
its actual path as described in [capability setup](docs/setup.md#capability-discovery).

**Simplified setup:** copy only `AGENTS.md` when the core guidance is sufficient.
Its built-in capability triggers and public sources remain available without the
curated reference. The two-file setup above is recommended for broader task guidance.

**Contributing or inspecting the source:** run
`git clone https://github.com/Liu-2026/AIBoot.git`, or
[download the ZIP](https://github.com/Liu-2026/AIBoot/archive/refs/heads/main.zip).
Clone obtains the source kit; application development uses your own project directory.
[See local-copy setup](docs/setup.md#inspect-and-add-the-core).

### 3. Open your tool in the destination project

- **Codex:** use root `AGENTS.md`, then start a fresh project session. If an
  `AGENTS.override.md` is active, follow its precedence and merge guidance into
  the effective entry. [Codex loading guide](adapters/codex/README.md).
- **Cursor:** use root `AGENTS.md`, open the project, and start a fresh Agent
  session. Keep scoped project rules for their existing purpose and avoid a
  second always-loaded copy of the core. [Cursor loading guide](adapters/cursor/README.md).
- **Claude Code:** use direct `AGENTS.md` loading in supported configurations.
  Where `CLAUDE.md` is the effective entry, preserve its content and add a
  project-local import: [Claude Code loading guide](adapters/claude-code/README.md).

```text
@AGENTS.md
```

The import above belongs in the effective `CLAUDE.md`, relative to that file.
Inspect your tool's loaded instructions or context view where available. Loading
follows the tool's version, settings, and instruction precedence.

### 4. Describe the project and start

You can speak in your preferred language. Here is a ready-to-use English example:

```text
Build a room-booking app for our small team.
Staff should view, create, and cancel bookings; overlapping bookings are disallowed.
Use a simple deployment we can maintain. Consider suitable existing solutions,
libraries, and native Skills or tools before choosing the implementation.
Establish the project brief and actionable plan in suitable project records.
Implement the agreed scope in working stages. Deliver usable run instructions
and an accurate account of verification and remaining work.
```

Provide real users, workflows, required behavior, constraints, and useful examples.
References or an existing plan help when you have them. AIBoot's guidance applies
through ordinary tasks; you can ask for planning first or authorize implementation.

## How to use AIBoot

### Research and plan before implementation

Use this when scope or technology choices need discussion:

```text
Plan an inventory tool for our operations team.
We need item search, stock adjustments, and CSV export.
Compare suitable existing solutions and choose an approach for our actual needs.
Record scope, acceptance examples, consequential decisions, milestones, and dependencies.
Plan only; do not implement or deploy yet.
```

The result should identify the agreed requirements, relevant choices, and next
work. Confirm the important choices, then ask the agent to implement the agreed plan.

### Develop against an agreed plan

```text
Implement the agreed scope in [plan or issue reference].
Check the current project state and finish the work in integrated stages.
Keep requirements connected to tasks, implementation, and completion evidence.
Update affected progress and decisions; make blockers or scope changes explicit.
```

For substantial work, the core calls for durable project knowledge. Existing
issues, plans, or documents can hold it. When the project has no suitable entry,
one concise project note can initially hold the brief, decisions, plan, and
progress. Split it when size, ownership, or use makes separate records worthwhile.

For example, a project may use `docs/project.md` for those facts and keep a short
pointer in `AGENTS.md`. That is a possible layout, not a required filename or a
fixed document package. Shared records follow your project's Git policies.

### Resume in a new session or hand off

```text
Continue from [current project record or issue reference].
Reconcile recorded progress with actual files and applicable evidence.
Complete the next agreed milestone and update the affected project records.
Leave the next action clear for the following session or collaborator.
```

Use native session recovery where available. A different tool or collaborator
can use the same durable records and effective instruction entry. At a milestone,
record meaningful changes, blockers, and the next action; unchanged facts need no
repeated report. [Continuity guide](docs/setup.md#continue-work-across-sessions).

### Make a small change

```text
Change [the specific behavior or text] to [the requested result].
Preserve unrelated behavior and existing conventions.
Review the affected change and perform relevant verification.
```

Routine edits use existing context and focused work. Requirements research and
architecture planning apply when the change actually needs them.

### Review delivery or prepare maintenance

```text
Review this milestone against the agreed requirements.
Connect each important requirement to its implementation and evidence.
Check usable run instructions and relevant integration or migration needs.
Report remaining, blocked, deferred, and unverified work accurately.
```

For refactoring, describe the demonstrated problem and expected behavior to
preserve. The core guides attention to affected interfaces, dependent modules,
and actual migration or rollback needs. Publishing or deploying follows your
existing authorization. See [more task prompts](docs/prompts.md).

## A connected engineering workflow

**Requirements → Research → Design & plan → Build & integrate → Verify & review → Deliver & continue**

For each important requirement, preserve its source and agreed status, an
observable acceptance example, related tasks and dependencies, implementation
references, and evidence or verification gaps. Use links and short labels in
existing records. Before closing a milestone, reconcile the full agreed scope.

For example: **“Prevent overlapping bookings” → booking-conflict task → booking
module → relevant behavior evidence.** A change to the rule updates the affected
plan, interfaces, and evidence. Progress reflects outcomes and current states,
with the basis of estimates made clear.

For multiple modules or permitted native subagents, agree interface contracts,
ownership of shared changes, and integration order. Keep responsibility for the
combined result explicit. Your coding tool manages collaboration and execution.
[Workflow guide](docs/setup.md#follow-the-development-workflow).

## Skills and tools at the right moment

**Describe the work. Put specialized capabilities to work where they matter.**

The core includes task triggers and discovery sources. At project start, a
material task change, or a specialized need, it guides your agent to match the
work to installed Skills, connected tools, and existing project methods.

- **Interface design:** suitable guidance such as Impeccable can help turn users,
  content, and visual references into a distinctive product direction.
- **SDKs and APIs:** a connected Context7 tool or official versioned documentation
  supplies relevant implementation references.
- **External services:** connected integrations and native plugin/MCP discovery
  help locate task-relevant service capabilities.
- **Specialist work:** select appropriate database, browser, security-review,
  mobile, and document-artifact methods for the actual need.

If a useful gap remains, focused upstream search, skills.sh, and public MCP
metadata supply candidates; private integrations use organization sources.
Your tool handles installation, loading, connections, permissions, and execution.
AIBoot adds selection and failure-recovery guidance; installing a reference file
alone does not connect a service or install third-party Skills.

### Use the included capability reference

The recommended setup includes `docs/aiboot-capabilities.md`, with ten curated
routes and selection/failure guidance. The core directs the agent to relevant
guidance when a specialized task appears. Installed Skills and connected tools remain preferred.
Routine edits and settled choices do not require rereading the catalog.

If the file lives elsewhere, record its actual path in the effective instruction
entry. The reference stays on demand; a Claude `@` import would instead load it as
instructions. [Capability setup](docs/setup.md#capability-discovery).

## Update AIBoot in your project

1. Obtain the new core and compare it with your installed version and local edits.
2. Merge the applicable changes, preserving your project conventions and records.
3. Record the source version or commit in the normal Git change description.
4. Refresh the tool's project session and inspect the effective instruction entry.

Update the paired capability reference through the same review. To remove AIBoot, remove its identified
guidance or import while retaining useful project facts and local modifications.
[Update and removal guide](docs/setup.md#update-and-remove).

## Inside the kit

```text
scaffold/AGENTS.md            # shared engineering playbook
scaffold/capabilities.md      # recommended routes, read on demand
adapters/                    # native loading guides
docs/setup.md                # detailed setup and lifecycle guide
docs/prompts.md              # planning, building, resuming, and delivery prompts
docs/assets/aiboot-hero.png   # project artwork
```

The core stays portable across stacks. Your product owns its application layout,
dependencies, tests, CI, documentation, and release process.

## Build with us

AIBoot is **open source under MIT**. Share a practical workflow, improve a
capability route, or help make the guidance sharper and easier to use.

- [Contributing](CONTRIBUTING.md) — contribution and Git workflow.
- [Setup guide](docs/setup.md) — project setup and lifecycle.
- [Task prompts](docs/prompts.md) — ready-to-adapt starting points.
- [Issues](https://github.com/Liu-2026/AIBoot/issues) — feedback, ideas, and examples.

**Give AIBoot a Star and help bring better engineering habits to AI development.**

## License

[MIT](LICENSE). Project artwork was created for AIBoot.
