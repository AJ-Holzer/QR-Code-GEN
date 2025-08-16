from env.config import config


def list_options() -> None:
    for option_name in config.AVAILABLE_OPTIONS:
        print(option_name)
