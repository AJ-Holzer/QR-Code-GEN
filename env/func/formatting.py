from env.config import config
import re
from typing import Match

# Compile regex pattern once for performance
TAG_PATTERN = re.compile(r"<[^>]+>")


def format_str(s: str) -> str:
    def repl(match: Match[str]) -> str:
        tag = match.group(0)
        return config.STRING_FORMATS.get(tag, tag)  # Keep unknown tags as is

    return TAG_PATTERN.sub(repl, s)
