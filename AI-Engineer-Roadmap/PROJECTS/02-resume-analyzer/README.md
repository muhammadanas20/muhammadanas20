# Resume Analyzer

**Phase:** 5+  
**Time:** 1–2 days

Extract a resume into a **pydantic** model: skills, years, education, claims.

## Why it is a good project

Structured output is the #1 production LLM skill. Evals are obvious (did we extract the right skills?).

## Must

- `Resume` pydantic model
- Temperature 0
- Retry once on `ValidationError`
- 10 labeled resumes (anonymized / fake)
- Accuracy table

## Security

Do not upload real people's resumes to a public model without consent. Use fake data in the public repo.
