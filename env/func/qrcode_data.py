from env.config import config
from env.func.formatting import format_str


def get_qr_code_data(option: str) -> str:
    # Create empty list holding the user values
    values: list[str] = []

    # Tell the user to input values
    print(format_str(s="\n<gray>Please enter the required values down below:<rst>"))

    # Get user decisions
    for question in config.AVAILABLE_OPTIONS[option]["inputs"]:
        values.append(input(f"> {question}: "))

    return config.AVAILABLE_OPTIONS[option]["format"].format(*values)
