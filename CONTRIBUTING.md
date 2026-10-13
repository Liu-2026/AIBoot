# Contributing to AIBoot

Useful contributions improve correct, usable, maintainable delivery. Necessary
analysis, design, documentation, and verification take priority over context or
process savings. Real examples, effective workflow guidance, clearer setup, and
removing duplicate or irrelevant work are all welcome.

## A small, reviewable change

Create a branch from `main`, make one coherent change, and open a pull request
against `main`. Existing commit messages use a short type and purpose, such as
`refactor: consolidate engineering guidance` or `docs: clarify local setup`.

- Explain the observed problem, expected behavior, and why existing native
  capabilities or current guidance are insufficient.
- Change distributable content in `scaffold/`; keep adapters focused on loading.
- Keep prompts in English and both READMEs aligned on setup, claims, and limitations.
- For trigger changes, include a relevant and an irrelevant task. Evaluate the
  outcome rather than enforcing one wording, stack, or sequence.
- Remove rules that no longer help. Avoid universal policies derived from one
  failure and do not turn a suggestion into a new requirement.
- A capability reference needs a concrete task need, a current upstream source,
  and an unsuitable case. Inspect the actual workflow and its setup effects;
  popularity alone is insufficient. Keep references optional, select relevant
  items from collections, and link upstream rather than mirroring Skills.
- For discovery changes, include an implicit task trigger and an unavailable-source
  or access-failure case. A successful directory lookup is separate from successful
  task use; source checks cannot prove automatic selection.

## Check the repository

Review changed local links, image references, loading instructions, and the
documented copy commands. Keep the English and Chinese READMEs aligned.

```sh
git diff --check
```

For loading changes, check the affected native entry and preserve existing project
instructions. For behavior comparisons, use fresh independent sessions with
identical task inputs and tools; keep evaluator notes out of the executing agent's
context. Report the checks actually performed and their results.

The public kit contains the scaffold and its usage documentation. Keep internal
planning, maintainer scripts, test fixtures, and validation records local and
ignored. AIBoot uses the host coding tool's native capabilities.

Do not add a runtime, installation service, external account, or model evaluation
runner without a demonstrated need. Keep raw run outputs and credentials out of
Git. Share small reproducible tasks and redacted evidence through issues or PRs.

## License and assets

Contributions are accepted under [MIT](LICENSE). Retain the required notices when
redistributing AIBoot content. The README uses original artwork generated for
AIBoot. Do not add third-party assets without documenting their source and
compatible licensing.
