# Common mistakes — Phase 1: Python refresh

### 1. async def with time.sleep

You blocked the loop. All chats freeze.

**Do this instead:** asyncio.sleep or to_thread.

### 2. except Exception: pass around await

You swallowed CancelledError and KeyboardInterrupt cousins.

**Do this instead:** Catch specific errors. Let CancelledError out.

### 3. Building a list of all tokens then joining

You used extra RAM and delayed first byte.

**Do this instead:** Yield chunks.

If you invent a new mistake, add it here in a PR. That is how this file stays alive.
