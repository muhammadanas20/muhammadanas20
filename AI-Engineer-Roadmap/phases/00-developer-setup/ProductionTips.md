# Production tips — Phase 0: Developer setup

## Cost

A leaked key is the expensive bug at this phase. Budget $0 for setup. Budget time for doing it once.

## Latency

WSL on /mnt/c can make `pip install` and Git feel like 2012. Move the repo.

## Reliability

Pin Python version. Write a sanity command. Run it in CI.

## Observability

Even now: print `sys.executable` in failing jobs. Future you will thank you.

## Scaling

Dotfiles do not scale a team. A repo with compose + README does.

## The boring checklist

- Python version documented
- .gitignore includes .venv and .env
- .env.example committed
- Sanity script in CI
- Docker Desktop (or Engine) starts cleanly

Production is not a later phase. It is a way of writing Tuesday's code.
