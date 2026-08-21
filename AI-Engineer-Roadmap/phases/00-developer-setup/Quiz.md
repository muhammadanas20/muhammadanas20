# Quiz — Phase 0: Developer setup

Closed notes. 80% to pass. Answers at the bottom. No scrolling first.

1. A command succeeded. Its exit code is:
    A) 1
    B) 0
    C) -1
    D) None
2. Why use a virtual environment?
    A) It makes Python faster
    B) It isolates project dependencies
    C) It replaces Docker
    D) It encrypts your code
3. Which file SHOULD be committed?
    A) .env
    B) .venv/
    C) .env.example
    D) id_rsa
4. On Windows, where should the Git repo live when using WSL2?
    A) C:\\Users\\you\\repo
    B) /mnt/c/Users/you/repo
    C) Inside the Linux home, e.g. ~/repo
    D) On a USB stick
5. What does Docker add that a venv does not?
    A) Type hints
    B) An isolated OS-level runtime plus system packages
    C) A faster Python
    D) Free GPUs
6. Port 8000 is already in use. First move?
    A) Reinstall Python
    B) Find the process bound to 8000 and stop it or pick another port
    C) Disable the firewall
    D) Delete .venv
7. `python` on PATH is 3.9, but `.venv` is 3.12. Which runs after activation?
    A) 3.9
    B) 3.12
    C) Both randomly
    D) Neither
8. The safest way to give GitHub your identity from a laptop is:
    A) Commit your password in .gitconfig
    B) SSH key or gh auth login
    C) Disable HTTPS
    D) Share a teammate's token
9. CI (GitHub Actions) most commonly runs on:
    A) Your laptop OS
    B) Linux VMs
    C) iOS
    D) DOS
10. You pasted an API key into a public commit then deleted the file in a new commit. The key is:
    A) Safe, Git forgets
    B) Still in history and must be rotated
    C) Encrypted automatically
    D) Only visible to you

---

<details>
<summary>Answers (spoiler)</summary>

1. **B** — Unix convention: 0 success, non-zero failure.
2. **B** — Isolation. Speed is unrelated. Docker is a different isolation layer.
3. **C** — Examples of names, never values.
4. **C** — /mnt/c is slow and causes permission weirdness.
5. **B** — venv isolates Python packages. Docker isolates the machine shape.
6. **B** — One listener per port.
7. **B** — Activation prepends `.venv/bin` to PATH.
8. **B** — Credential helpers / SSH. Never a password in Git.
9. **B** — ubuntu-latest is the default. Test Linux early.
10. **B** — History keeps blobs. Rotate the secret. Then rewrite history if needed.

</details>
