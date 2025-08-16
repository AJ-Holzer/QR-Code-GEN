from typing import TypedDict


class InputOption(TypedDict):
    inputs: list[str]
    format: str


InputOptions = dict[str, InputOption]
