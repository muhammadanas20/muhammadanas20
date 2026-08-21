# GitHub Actions

```yaml
name: ci
on:
  pull_request:
  push:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: "3.12" }
      - run: pip install -r requirements.txt
      - run: ruff check .
      - run: pytest -q
```

Add a `deploy` job `needs: test` that builds and pushes `ghcr.io/<you>/<app>:${{ github.sha }}`.

Prefer OIDC to clouds over long-lived access keys.

Secrets: repository Settings → Secrets. Never echo them.
