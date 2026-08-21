# Flashcards — Phase 0: Developer setup

Say the answer. Then open. Do the deck two days later. That is the whole spaced-repetition system.

**Q1.** Exit code 0 means?

<details><summary>Answer</summary>

Success.

</details>

**Q2.** What folder is a venv usually called?

<details><summary>Answer</summary>

.venv (or venv).

</details>

**Q3.** Name two things that must be gitignored.

<details><summary>Answer</summary>

.venv and .env (and __pycache__).

</details>

**Q4.** What is a port?

<details><summary>Answer</summary>

A number a process binds so others can talk to it on that machine.

</details>

**Q5.** WSL repos should live where?

<details><summary>Answer</summary>

In the Linux filesystem, not under /mnt/c.

</details>

**Q6.** venv vs Docker in one line?

<details><summary>Answer</summary>

venv isolates Python packages; Docker isolates the whole runtime.

</details>

**Q7.** What is PATH?

<details><summary>Answer</summary>

Directories the shell searches for executables.

</details>

**Q8.** Why lock files?

<details><summary>Answer</summary>

Same dependency versions on every machine and in CI.

</details>

**Q9.** What does uv replace for many people?

<details><summary>Answer</summary>

pip + venv + pip-tools, faster.

</details>

**Q10.** First thing to check on ModuleNotFoundError?

<details><summary>Answer</summary>

Which python (sys.executable) and whether the venv is active.

</details>
