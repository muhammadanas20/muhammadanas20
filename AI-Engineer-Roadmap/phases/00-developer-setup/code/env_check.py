"""Read configuration from the environment. Never print secrets."""
from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_env: str
    openai_api_key: str | None

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            app_env=os.getenv("APP_ENV", "development"),
            openai_api_key=os.getenv("OPENAI_API_KEY"),
        )


def main() -> None:
    settings = Settings.from_env()
    print("APP_ENV=", settings.app_env)
    print("OPENAI_API_KEY set=", bool(settings.openai_api_key))


if __name__ == "__main__":
    main()
