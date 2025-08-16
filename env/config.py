from env.typing.options import InputOptions


class Config:
    AVAILABLE_OPTIONS: InputOptions = {
        "URL": {
            "inputs": ["Enter URL"],
            "format": "{}",
        },
        "Wi-Fi": {
            "inputs": [
                "Enter SSID",
                "Enter Wi-Fi password",
                "Wi-Fi network is hidden (true/false)",
            ],
            "format": "WIFI:T:WPA;S:{};P:{};H:{}",
        },
        "Phone Number": {
            "inputs": ["Enter phone number"],
            "format": "tel:{}",
        },
        "Email": {
            "inputs": ["Enter email address"],
            "format": "mailto:{}",
        },
        "SMS": {
            "inputs": ["Enter phone number", "Enter SMS message"],
            "format": "smsto:{}:{}",
        },
        "VCard": {
            "inputs": [
                "Full Name",
                "Last Name",
                "First Name",
                "Nickname",
                "Organization",
                "Title",
                "Phone (cell)",
                "Phone (work)",
                "Email (home)",
                "Email (work)",
                "Home Address (Street, City, Region, Postal, Country)",
                "Work Address (Street, City, Region, Postal, Country)",
                "Website",
                "Birthday (YYYYMMDD)",
                "Note",
            ],
            "format": """
                BEGIN:VCARD
                VERSION:3.0
                FN:{}
                N:{};{};;;
                NICKNAME:{}
                ORG:{}
                TITLE:{}
                TEL;TYPE=cell:{}
                TEL;TYPE=work:{}
                EMAIL;TYPE=home:{}
                EMAIL;TYPE=work:{}
                ADR;TYPE=home:;;{}
                ADR;TYPE=work:;;{}
                URL;TYPE=work:{}
                BDAY:{}
                NOTE:{}
                END:VCARD
                """,
        },
    }

    STRING_FORMATS: dict[str, str] = {
        # Reset
        "<rst>": "\033[0m",
        # Text styles
        "<bold>": "\033[1m",
        "<dim>": "\033[2m",
        "<italic>": "\033[3m",  # ⚠️ Not always supported
        "<underline>": "\033[4m",
        "<blink>": "\033[5m",
        "<reverse>": "\033[7m",  # Swap fg/bg
        "<hidden>": "\033[8m",
        "<strike>": "\033[9m",  # ⚠️ Not always supported
        # Foreground colors
        "<black>": "\033[30m",
        "<red>": "\033[31m",
        "<green>": "\033[32m",
        "<yellow>": "\033[33m",
        "<blue>": "\033[34m",
        "<magenta>": "\033[35m",
        "<cyan>": "\033[36m",
        "<white>": "\033[37m",
        "<default>": "\033[39m",
        # Bright foreground colors
        "<gray>": "\033[90m",
        "<bred>": "\033[91m",
        "<bgreen>": "\033[92m",
        "<byellow>": "\033[93m",
        "<bblue>": "\033[94m",
        "<bmagenta>": "\033[95m",
        "<bcyan>": "\033[96m",
        "<bwhite>": "\033[97m",
        # Background colors
        "<bg_black>": "\033[40m",
        "<bg_red>": "\033[41m",
        "<bg_green>": "\033[42m",
        "<bg_yellow>": "\033[43m",
        "<bg_blue>": "\033[44m",
        "<bg_magenta>": "\033[45m",
        "<bg_cyan>": "\033[46m",
        "<bg_white>": "\033[47m",
        "<bg_default>": "\033[49m",
        # Bright background colors
        "<bg_gray>": "\033[100m",
        "<bg_bred>": "\033[101m",
        "<bg_bgreen>": "\033[102m",
        "<bg_byellow>": "\033[103m",
        "<bg_bblue>": "\033[104m",
        "<bg_bmagenta>": "\033[105m",
        "<bg_bcyan>": "\033[106m",
        "<bg_bwhite>": "\033[107m",
    }


config = Config()
