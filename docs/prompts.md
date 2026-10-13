# Start work with AIBoot

[English overview](../README.md) · [中文概览](../README.zh-CN.md) · [Setup](setup.md)

Use these ordinary-language prompts after adding the core to your own project's
native instruction entry. Replace the bracketed context with real facts. They
work through the host's existing planning, tools, permissions, and recovery.
Choose the prompt for the stage you actually want.

## Start a new project

```text
Build [the product] for [the users and their workflows].
The agreed scope is [required behaviors], with [actual constraints].
Use the project guidance to investigate suitable existing solutions and choose
the approach. Establish the project brief, significant decisions, and actionable
plan in suitable project records. Implement the agreed scope in working stages
and deliver usable instructions with an accurate account of verification.
```

For a substantial project, a single existing document or issue can initially
hold the brief, decisions, plan, and progress. Split records when their size,
ownership, or use actually benefits from separate homes.

## Research and plan only

```text
Plan [the product or feature] for [the users and workflows].
Consider [actual constraints] and suitable existing solutions.
Define scope and acceptance, consequential design choices, milestones,
dependencies, and completion evidence in the normal project records.
Do not implement or deploy yet.
```

## Implement an agreed plan

```text
Implement the agreed scope in [plan or issue reference].
Check the current project state and keep requirements connected to tasks,
implementation, and completion evidence. Finish the authorized scope in
integrated stages; keep any blocker or proposed scope change explicit.
```

## Resume or hand off

```text
Continue from [current project record or issue reference].
Reconcile the recorded status with actual files and applicable evidence.
Finish the next agreed milestone, update affected progress and decisions,
and leave the next action clear for the following session or collaborator.
```

## Make a routine change

```text
Change [the specific behavior or text] to [the requested result].
Keep unrelated behavior and existing conventions intact.
Review the affected change and perform the relevant verification.
```

Existing context can supply the scope and conventions; this task needs no new
project-startup or document bundle.

## Review readiness for delivery

```text
Review [the milestone or release scope] against the agreed requirements.
Reconcile each important requirement with implementation and evidence.
Check usable run instructions and relevant integration or migration needs.
Report missing, blocked, deferred, and unverified work accurately.
Do not publish or deploy without existing authorization.
```

## Maintain or refactor

```text
Address [the demonstrated maintenance problem] in [affected area].
Identify behavior and interface commitments, dependent modules, and any actual
data migration or rollback needs. Plan and implement the relevant change while
preserving agreed behavior and checking the affected result.
```

If an activity is excluded, state it explicitly, such as `Do not run tests in
this task; report verification as not run.` That boundary changes the permitted
work, and the delivery report should reflect the resulting evidence status.

## Use a specialized capability

Describe the actual UI, SDK, database, artifact, or service task. The default core
already contains capability triggers and discovery entry points. For more detail,
give the agent the relevant section of [the optional reference](../scaffold/capabilities.md)
using [the optional setup](setup.md#optional-capability-discovery).
The host handles availability, loading, connection, and authorization.
