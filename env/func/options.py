from env.config import config
from env.func.formatting import format_str


def list_options() -> None:
    # Print header
    print(format_str(s="<bold>Available Options:<rst>"))

    # Print options
    print(
        "\n".join(
            f"  [{idx}] {option}" for idx, option in enumerate(config.AVAILABLE_OPTIONS)
        )
    )


def get_option() -> str:
    return list(config.AVAILABLE_OPTIONS.keys())[
        int(input(format_str(s="\n<gray>Select an option (default=0): <rst>")) or 0)
    ]
