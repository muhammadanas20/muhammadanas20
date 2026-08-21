# Course generators

`build.py` renders Markdown for all 15 phases from `phases/pXX.py`.

You only need this if you are **editing the course**, not taking it.

```bash
cd AI-Engineer-Roadmap
python scripts/build.py
```

Do not hand-edit generated phase Markdown if you also edit the Python sources — you will lose work on the next build. Change `scripts/phases/pXX.py` instead.
