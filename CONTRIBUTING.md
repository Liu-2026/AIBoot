# Contributing to AIBoot

Useful contributions make agent decisions better without adding unnecessary
context or process. Real examples, narrower triggers, clearer setup, and removing
unhelpful guidance are all welcome.

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

Python 3.9+ is needed only for maintainer checks, not to use AIBoot:

```sh
python3 scripts/check.py
python3 -m unittest discover -s tests
git diff --check
```

The checker covers local Markdown links, image references, and source-file
structure. Tests cover the checker and documented core copy guard in temporary
directories. These checks do not demonstrate useful agent behavior. For comparisons,
use fresh independent sessions with identical task inputs and tools; keep evaluator notes
out of the executing agent's context. Report actual results, including not-run checks.

Do not add a runtime, installation service, external account, or model evaluation
runner without a demonstrated need. Keep raw run outputs and credentials out of
Git. Share small reproducible tasks and redacted evidence through issues or PRs.

## License and assets

Contributions are accepted under [MIT](LICENSE). Retain the required notices when
redistributing AIBoot content. The README uses original artwork generated for
AIBoot. Do not add third-party assets without documenting their source and
compatible licensing.
