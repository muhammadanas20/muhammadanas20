# Solutions — Phase 0: Developer setup

Spoilers. Try for 25 minutes first.

We give **hints and approaches**, not copy-paste repos. If you paste a full solution into your portfolio without understanding it, the interview will hurt.

### B1 .gitignore

Put `.env` not `.env*`. The star would hide `.env.example`.

<details><summary>Approach (still not full code)</summary>

List: `.venv/`, `.env`, `__pycache__/`, `*.pyc`, `.pytest_cache/`. Commit `.env.example`.

</details>

### M2 pre-commit

pre-commit.com, ruff hook, `pre-commit install`.

<details><summary>Approach (still not full code)</summary>

Add `.pre-commit-config.yaml` with ruff and ruff-format. Keep excludes small.

</details>

### Assignment README

Three commands. One troubleshooting section. No autobiography.

<details><summary>Approach (still not full code)</summary>

Copy the style of this course's top README. Short paragraphs. Copy-pasteable blocks.

</details>

Full working patterns related to this phase also live in [`code/`](./code/) and [EXAMPLES](../../EXAMPLES/).
