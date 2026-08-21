# PaaS cheat sheet

Pick **one**. Finish.

## Fly.io

- `fly launch` from a Dockerfile
- `fly secrets set OPENAI_API_KEY=...`
- Health checks in `fly.toml`
- Regions: put app near DB

## Render

- Web service from Dockerfile or repo
- `PORT` env provided — read it
- Separate Postgres add-on
- Watch SSE timeouts

## Railway

- Similar DX to Render
- Volume only if you must (prefer managed PG)

## Common fails

- Listening on 127.0.0.1
- Ignoring `PORT`
- Scale-to-zero on a live demo
- Secrets in the Dockerfile
