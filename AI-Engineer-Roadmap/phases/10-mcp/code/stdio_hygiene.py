"""stdout is the protocol. Log to stderr."""
import sys


def log(msg: str) -> None:
    print(msg, file=sys.stderr)


if __name__ == "__main__":
    log("server starting")
