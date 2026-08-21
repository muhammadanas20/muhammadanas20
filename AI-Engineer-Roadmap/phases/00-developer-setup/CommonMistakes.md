# Common mistakes — Phase 0: Developer setup

### 1. Global package installs

`sudo pip install tensorflow` on the system Python. One month later nothing uninstalls cleanly.

**Do this instead:** venv per project. Or uv.

### 2. Committing .env because 'it's just a school key'

Bots scrape GitHub for `sk-` prefixes continuously.

**Do this instead:** .gitignore + secret scanning. Rotate if leaked.

### 3. Spaces in project paths

`~/My Documents/AI Course` will break naive scripts and Docker volume mounts.

**Do this instead:** `~/work/ai-engineer`.

### 4. Ignoring CI because 'it works locally'

Actions runs Linux. Your Mac hid the bug.

**Do this instead:** Green CI is part of the exit ticket.

If you invent a new mistake, add it here in a PR. That is how this file stays alive.
