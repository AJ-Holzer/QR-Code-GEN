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


config = Config()
