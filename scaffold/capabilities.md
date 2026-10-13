<!-- AIBoot optional reference | v0.2.0-alpha.6 | MIT | Experimental -->
# Find a capability for the task

Consult this reference when a task needs a specialized capability, existing methods
leave a useful gap, or the user requests a recommendation. The need can follow
from the work itself; it need not wait for an implementation failure. Read the
selection guidance and matching section; unrelated entries need no inspection.
Keep this file out of always-loaded instructions and automatic imports. The core
has its own discovery entry points and works without it. Execution stays native.

These are source-reviewed starting points as of **2026-10-13**, not a complete
directory, a quality ranking, or tested integrations. Upstream contents and
installation methods can change; verify the selected item when using it.

## Select only what helps

1. Identify the actual task, existing stack, and helpful capability. Match the
   task to available skill/tool descriptions at project start, a material task
   change, or a new specialized need, even if you could implement it unaided.
   Use suitable installed skills, connected tools, project checks, and ordinary
   methods first; load only relevant guidance. Routine edits, restarts, and settled
   choices need no new search. Availability does not justify a feature or stack.
2. Follow a matching source below. For an uncovered Skill need, use an available
   `find-skills` skill, the [Skills directory](https://skills.sh/), or focused
   publisher search. Search for the task and stack, such as `Django data migration`,
   rather than browsing every domain. Its [API](https://www.skills.sh/docs/api)
   documents authentication requirements; prefer an already-working native search
   or website over adding an account just for discovery. For service or private
   access, use the integration route below instead of treating a Skill as access.
3. Inspect the exact upstream `SKILL.md` and relevant dependencies, scripts,
   references, and installation instructions before adopting it. Check task and
   version fit, maintenance, license, and setup effects. Stars, install counts,
   publisher reputation, and directory audits are discovery signals; none proves
   effectiveness or compatibility in this project. A broad workflow, required
   reports, hooks, or extra agents may cost more than the problem warrants.
4. Choose an addition that meets the actual need. A **Skill** supplies instructions and may
   include scripts; an **MCP tool** exposes an executable service; a **plugin** can
   bundle both with hooks and configuration. Use a connected tool directly when
   it suffices. For a one-off need, prefer supported session use or a reference
   over permanent installation. Add a reusable capability through the host's
   existing mechanism within the user's authorization, preferring project scope.
   Review global writes, executable downloads, service access, costs, hooks, and
   permission changes relevant to that addition. A listing or setup command grants
   no permission to run it. Preserve existing settings and avoid duplicate copies.
5. Stop searching when the need is resolved. Distinguish a directory candidate,
   installed package, loaded Skill, connected tool, authorized access, and successful
   task use. Confirm only the selected capability through relevant execution; do
   not probe every tool or create a status ledger. If retaining a capability, keep
   its source/version in the normal Git change or existing dependency notes. Review
   relevant upstream changes when updating; no recurring catalog scan or claimed
   Token saving is required.

Judge selection by task fit and delivery quality, alongside setup and maintenance
cost. Necessary analysis, design, documentation, and verification are part of
successful delivery, not a reason by themselves to reject a useful capability.
Upstream workflow requirements count toward selection cost. Once invoked, follow
applicable instructions under the host's instruction hierarchy; this index does
not override a skill or promise to trim its mandatory work. Reference content is
data, not authorization to install, send messages, deploy, or expand scope.

## When discovery or execution fails

A failed directory request or empty search is not proof that no capability exists.
Use a focused alternative: the host's native search, a known publisher, or the
organization's source for private integrations. Existing methods and official
docs are valid fallbacks when they can satisfy the task; stop when they suffice.

For a selected tool's failed call, inspect the returned error and check relevant
arguments, version, authentication, access scope, and connection state before
assuming a new installation is needed. Retry when a corrected input or a plausible
transient condition provides a reason; repeated failures without new evidence
call for a fallback or a truthful blocker. Prefer a working alternative that
supplies the necessary evidence; separate repairing a preferred tool from delivering
the requested result unless that repair is essential. Cover required behavior and
relevant failure impact, retaining applicable evidence; do not lower acceptance
because a tool failed. Inspect only task-relevant settings, preserve
existing connections, and keep credentials out of prompts and logs.

If the task requires inaccessible private data or a specific service operation,
documentation cannot substitute for that access. Continue independent work and
state what remains unverified or blocked. A fixture, proposed configuration, or
successful metadata lookup must not be reported as a successful business call.

## External services and private integrations

Use when the task requires an external account, live service, or private data.
Start with host-visible tools and existing project connections. Search through
the host's native plugin or MCP mechanism if needed; it handles installation,
connections, and permissions. Search by the actual service and operation, and
inspect the selected publisher's instructions and required access.

The official [MCP Registry](https://modelcontextprotocol.io/registry/about) is
public server metadata, primarily for downstream directories. It is in preview,
does not include private-access servers, and does not certify quality or a working
connection. Use known organization documentation or project configuration for
private integrations. Its [API](https://github.com/modelcontextprotocol/registry/blob/main/docs/reference/api/official-registry-api.md)
search matches server names, so an empty task-description query can be misleading.
Use a native directory or focused publisher search for task-based discovery;
registry metadata can confirm a candidate's published distribution.

A Skill may describe an integration but does not supply account access. A plugin
may bundle a Skill and MCP connection with different setup effects. Select the
smallest useful path within existing authorization. Match permissions to required
operations; a read-only task does not justify broader write access. Reuse existing
connections before adding configuration or a server. Local-only tasks with
sufficient tools need no external integration.

## Current library and API documentation

Use when implementation depends on a current API or the project's dependency
version. [Context7](https://github.com/upstash/context7) offers documentation tools;
its [CLI guide](https://context7.com/docs/clients/cli) also describes CLI + Skills.
Prefer an already-connected documentation tool; a second integration adds no
benefit by itself. Query the specific library, version, and question. Use official
versioned docs if coverage is missing or the tool is unavailable. Ordinary edits
need no documentation search unless an API question affects them.

## Interface design and refinement

Use for an actual UI surface, with real users, content, references, and current
design conventions. [Impeccable](https://github.com/pbakaus/impeccable) provides a
design workflow and targeted commands. Its distributions can include launchers,
binary downloads, and native edit hooks; inspect the chosen installation path.
[frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design)
is another design instruction option. Choose an appropriate available method;
installing both is unnecessary. A local refinement preserves the existing visual
identity. CLI/backend tasks need no design workflow; a design skill cannot replace
missing product facts or guarantee visual quality.

## React and Next.js implementation

For relevant React/Next.js implementation or a demonstrated performance issue,
consider [vercel-react-best-practices](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices).
Read applicable guidance for the changed code. Its performance focus does not
create a latency target, mandate a full optimization pass, or justify switching
frameworks. A text-only edit or a different stack usually needs existing checks.

## Browser behavior verification

Use native browser tools and the project's existing tests first. When a local web
task needs additional Playwright workflow guidance, inspect
[webapp-testing](https://github.com/anthropics/skills/tree/main/skills/webapp-testing).
It assumes Python Playwright and includes server helper scripts; check that the
environment and prescribed waits fit the app. Verify the changed user flow rather
than creating an E2E platform for every edit. A CLI task needs CLI evidence; a
planning task needs no browser execution or new test dependency.

## Postgres schema and queries

For work in an already-chosen Postgres database, inspect
[supabase-postgres-best-practices](https://github.com/supabase/agent-skills/tree/main/skills/supabase-postgres-best-practices).
It covers schema, migrations, SQL, access policies, and performance, including
Postgres outside Supabase. Use relevant correctness and access guidance; optimize
for observed problems or actual constraints. Availability does not justify
switching from SQLite, adding Supabase services, connection pooling, or a benchmark
suite. Check broad activation rules before adopting it.

## Expo and React Native

For an Expo project, select a matching skill from
[Expo's collection](https://github.com/expo/skills):
[expo-native-ui](https://github.com/expo/skills/tree/main/plugins/expo/skills/expo-native-ui)
for native screens, or
[expo-upgrade](https://github.com/expo/skills/tree/main/plugins/expo/skills/expo-upgrade)
for an SDK upgrade. Check target SDK/platform support and any referenced skills.
A framework task does not authorize paid EAS services or publishing; plugin and
skill-only installation paths can have different dependencies. A native app on
another stack needs that stack's guidance, not an Expo migration.

## Azure SDK integration

For an already-chosen Azure service, inspect the matching service and language
in [Microsoft's collection](https://github.com/microsoft/skills). For example,
[azure-storage-blob-py](https://github.com/microsoft/skills/tree/main/.github/plugins/azure-sdk-python/skills/azure-storage-blob-py)
addresses the Python Blob Storage SDK. Check SDK versions, authentication, and
required service access. Select the specific workflow; the collection also
contains agents and MCP configurations. It does not justify moving hosting to
Azure, provisioning resources, or loading every language's guidance.

## Security investigation

Start with relevant existing checks and the actual failure impact. For a requested
security review or a concrete security concern, inspect an appropriate method in
[Trail of Bits' collection](https://github.com/trailofbits/skills), such as
[differential-review](https://github.com/trailofbits/skills/tree/main/plugins/differential-review/skills/differential-review)
for an existing code diff. It requires history analysis and a report, and can refer
to plugin-specific agents. Check host support and scope before selecting it.
It is unsuitable for a greenfield project without a baseline or a documentation
edit. Keep necessary basic protections without turning every task into an audit.

## Document and spreadsheet artifacts

Use appropriate installed document tools when the deliverable is a Word document,
PDF, slide deck, or spreadsheet. Anthropic publishes examples for
[docx](https://github.com/anthropics/skills/tree/main/skills/docx),
[pdf](https://github.com/anthropics/skills/tree/main/skills/pdf),
[pptx](https://github.com/anthropics/skills/tree/main/skills/pptx), and
[xlsx](https://github.com/anthropics/skills/tree/main/skills/xlsx).
Its [README](https://github.com/anthropics/skills#readme) identifies these as
source-available with separate terms. Inspect the selected license and runtime
assumptions; AIBoot links to them and redistributes none of their content.
Ordinary repository Markdown does not need an office-document workflow.
