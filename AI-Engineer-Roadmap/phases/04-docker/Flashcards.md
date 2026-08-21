# Flashcards — Phase 4: Docker

Say the answer. Then open. Do the deck two days later. That is the whole spaced-repetition system.

**Q1.** Image vs container?

<details><summary>Answer</summary>

Image = snapshot. Container = running instance.

</details>

**Q2.** Why slim?

<details><summary>Answer</summary>

Smaller, fewer packages, smaller attack surface.

</details>

**Q3.** DNS name of a compose service?

<details><summary>Answer</summary>

The service key, e.g. postgres.

</details>

**Q4.** What does -p 8000:8000 mean?

<details><summary>Answer</summary>

Host 8000 → container 8000.

</details>

**Q5.** Why not copy .venv?

<details><summary>Answer</summary>

Wrong OS/arch; huge; shadows image packages.

</details>

**Q6.** Bind mount use?

<details><summary>Answer</summary>

Live code in dev.

</details>

**Q7.** Multi-stage?

<details><summary>Answer</summary>

Build in one image, copy artifacts to a small runtime image.

</details>

**Q8.** Where do logs go?

<details><summary>Answer</summary>

Stdout/stderr so the platform collects them.

</details>

**Q9.** Secret in Dockerfile ENV?

<details><summary>Answer</summary>

Lives in image history. Don't.

</details>

**Q10.** init: true?

<details><summary>Answer</summary>

Reap zombie processes.

</details>
