# Design: voice assistant

ASR stream → LLM stream → TTS. Barge-in (cancel TTS on new speech).

TTFT matters more. Smaller / faster models. Regional data if needed.

Eval: WER of ASR plus task success.

Privacy: audio retention policy. Don't send raw audio to five vendors without a contract.
