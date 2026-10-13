# Add AIBoot to a project

[English overview](../README.md) · [中文概览](../README.zh-CN.md)

The kit is `v0.2.0-alpha.8`: a core guidance file plus a recommended capability
reference read on demand. Your coding tool loads the core and executes the work.
Existing project conventions, native plans, checks, and appropriate installed
Skills continue to supply the rest of the workflow.

## Choose your project directory

For your own software, create or open its own project directory and Git repository.
Keep AIBoot as the source of the engineering guidance; your product owns its code,
README, history, license, and project records. A framework starter can supply the
application structure after the agent has chosen an appropriate stack.

Cloning AIBoot obtains the kit and its references. Its distributable core lives
at `scaffold/AGENTS.md`; add that content to your destination project's native
entry to activate the workflow there. Developing AIBoot itself uses the kit
repository and its local maintainer guidance.

## Pull the recommended complete kit

Run the platform snippet in your own project root. Pull only the core, capability
reference, and MIT notice; a source checkout is unnecessary for normal use.
The snippets stage all downloads before writing destinations and stop if a target
already exists. They do not execute downloaded scripts or alter Git remotes.
Use an exact commit instead of `main` to pin all downloads to a fixed revision.
On failure, inspect the actual error and destination files before trying again.

### macOS / Linux

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

### Windows PowerShell

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

### Manual download and existing instructions

Download [the core](https://raw.githubusercontent.com/Liu-2026/AIBoot/main/scaffold/AGENTS.md),
[the capability reference](https://raw.githubusercontent.com/Liu-2026/AIBoot/main/scaffold/capabilities.md),
and [the MIT notice](https://raw.githubusercontent.com/Liu-2026/AIBoot/main/LICENSE).
Save or merge them as `AGENTS.md`, `docs/aiboot-capabilities.md`, and
`docs/aiboot-LICENSE`. Preserve existing conventions and an identifiable source
version. Preserve an existing third-party notice instead of adding a duplicate
when it already contains the required AIBoot MIT text.

The core points to `docs/aiboot-capabilities.md` at relevant task triggers. If you
choose another location, record its actual path in the effective instruction entry
as described under [capability discovery](#capability-discovery).
Existing higher-priority native entries still follow the adapter's loading rules.

## Inspect and add the core

Get a local copy using your Git host's clone or Download ZIP action. Run this
POSIX-shell example in the destination project on macOS/Linux. On Windows, copy
the same file using your file manager or editor.

You can also [download only the core](https://raw.githubusercontent.com/Liu-2026/AIBoot/main/scaffold/AGENTS.md)
and save its content as `AGENTS.md` in the destination project root. Merge with an
existing entry instead of replacing it. This simplified setup retains core discovery
guidance. Pair it with the reference for the recommended complete setup.

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

Open the destination directory in the coding tool, use its effective native entry,
and start a fresh session. If a higher-priority override is active, merge applicable
guidance into that entry as described by the adapter. Use
[the task prompts](prompts.md) to start planning, implement, resume, review, or
prepare a delivery through ordinary language.

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

## Follow the development workflow

The core prioritizes a correct, usable, maintainable outcome. Spend the effort
needed for analysis, documentation, design, implementation, and verification.
Reduce duplication and irrelevant work while preserving agreed scope and quality.

For a new project or substantial feature, establish users, workflows, business
rules, scope, constraints, and acceptance examples. Investigate existing solutions
and suitable capabilities. Explain consequential choices, relevant module/data
boundaries, and interfaces before implementing work that depends on them.

Keep an actionable plan for multi-step work: milestones, task dependencies,
completion evidence, and current status. A durable project brief and significant
decisions belong in existing plans, issues, or documents; one shared entry can
contain them. When a suitable entry is missing, create it in the normal project
location. Expand records as the project's decisions and coordination need grow.
The core specifies needed information rather than a fixed document bundle.

Build connected units and check their integration. Distinguish planned,
in-progress, implemented-but-unverified, verified, and blocked work. Review the
actual changes and verify affected business rules, important boundary/failure
cases, and relevant integrations. Choose checks from the result and impact;
use actual runtime, browser, or service evidence when those behaviors matter.
An unavailable tool calls for a sufficient alternative or an explicit blocker,
not a weaker acceptance condition.

Before delivery, check the requested scope, setup/run instructions, and required
configuration, migration, or deployment steps. A first working slice is a
milestone; continue the remaining authorized work unless the user requested that
milestone or prototype as the whole deliverable. Keep ongoing operating and
maintenance needs visible when the product requires them.

For example, a small booking application can use the existing server and a
maintained framework while still checking appointment conflicts, relevant access
rules, persistence, and usable setup. A change spanning existing modules can
require interface decisions, dependency sequencing, broader regression checks,
and a migration/rollback plan. Routine help-text edits use established context
and relevant checks without repeating project design.

## Keep requirements connected to delivery

In the existing plan, issue, or project record, connect each important requirement
to its source/agreed status, observable acceptance, tasks and dependencies,
implementation references, and verification evidence or gaps. Short labels and
links are enough; a separate traceability document is optional.

For example, a room-booking requirement can point to its agreed overlap rule,
the booking-validation task, the implementation module, and the relevant result.
If that result has not been checked, its status remains implemented-but-unverified.
At delivery, reconcile all in-scope requirements; retain missing, deferred,
blocked, and unverified items instead of counting them as complete.

Scope changes update affected decisions, interfaces, tasks, and acceptance. Keep
the reason and current agreement in the existing record. Progress can be reported
as verified milestone outcomes and counts by task state; percentages need a clear
basis and must account for tasks that differ in size and uncertainty.

When the user excludes testing, record that omission and distinguish the delivered
implementation from verified acceptance. The workflow follows the user's stage
and authorization; omitted checks do not acquire a passing result.

## Continue work across sessions

Multi-stage projects need durable goals, significant decisions, an actionable
plan, and current progress. Use native recovery alongside existing plans, issues,
or project documents. If no suitable durable entry exists, keep one concise
project note in the normal document location. There is no required filename or
document bundle; sufficient existing records need no duplicate ledger.

If needed, add a short path or issue reference to the native instruction entry
so later sessions can locate these records. Keep the details in their own source
and read them when relevant.

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
The setup adds guidance files, not AIBoot's `.gitignore`. Your project's shared plans,
conventions, and decisions follow its own collaboration and versioning needs.

For work across modules or native subagents, establish interface contracts,
ownership of shared changes, and integration order. Use authorized native
collaboration and project records to coordinate dependency changes. Review the
combined result against the same requirements. For maintenance or refactoring,
address behavior compatibility and actual data migration/rollback needs before
changing dependent implementations.

<a id="optional-capability-discovery"></a>

## Capability discovery

The core includes task triggers, direct public discovery sources, and failure
guidance. Describe the actual work; it can match suitable installed capabilities
without a Skill name in the task. New specialized needs can justify discovery;
ordinary edits and restarts do not require it. The recommended setup includes the
capability reference; the simplified setup can use the core alone.

The recommended direct download puts
[the capability reference](../scaffold/capabilities.md) at
`docs/aiboot-capabilities.md`, where the core routes relevant tasks to it. You can
also attach it or provide its actual local path for session-specific use. It contains
selection guidance and ten task-specific routes, including MCP/private integrations and failure paths,
not installed Skills or tools.

To retain the reference in a destination project, inspect its existing document
layout and copy it manually, or use this guarded POSIX-shell example:

```sh
AIBOOT_SOURCE="/absolute/path/to/AIBoot"
test ! -e docs/aiboot-capabilities.md && test ! -L docs/aiboot-capabilities.md && \
  mkdir -p docs && \
  cp "$AIBOOT_SOURCE/scaffold/capabilities.md" docs/aiboot-capabilities.md
```

The current core already includes the default path. For a custom location or an
older merged entry, add or adjust this pointer in the effective native entry:

```text
When a task needs a specialized capability or existing methods leave a useful gap,
consult the selection guidance and matching section of docs/aiboot-capabilities.md
before choosing an approach. Prefer suitable installed Skills and connected tools.
Read it on demand; do not import it into always-loaded context. Execution stays native.
```

Use a plain pointer, not a Claude `@` import, duplicate always-on rule, or skill
wrapper. With the simplified core-only setup, agents can still use installed
capabilities and discover upstream sources. A copied reference uses external
links and remains independent of the original AIBoot checkout.

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
identifiable AIBoot guidance, an import, or a capability reference pointer added for
it. Keep project facts, local conventions, user modifications, and required notices
for content retained.
A formerly AIBoot-owned file with useful project content needs editing, not
automatic deletion.

Review the paired capability reference through the same update process. Remove only
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

File copying and source-format checks establish different facts from useful agent
behavior. Native loading, task outcomes, cross-tool coexistence, and remote/cloud
use each need evidence appropriate to the actual environment.
