import os
from env.func.options import list_options, get_option
from env.func.formatting import format_str
from env.func.qrcode_data import get_qr_code_data
from env.func.qrcode import create_qr_code


def main() -> None:
    print(
        format_str(
            s=r"""<gray>
         _______  _______         _______  _______  ______   _______    _______  _______  _       
        (  ___  )(  ____ )       (  ____ \(  ___  )(  __  \ (  ____ \  (  ____ \(  ____ \( (    /|
        | (   ) || (    )|       | (    \/| (   ) || (  \  )| (    \/  | (    \/| (    \/|  \  ( |
        | |   | || (____)| _____ | |      | |   | || |   ) || (__      | |      | (__    |   \ | |
        | |   | ||     __)(_____)| |      | |   | || |   | ||  __)     | | ____ |  __)   | (\ \) |
        | | /\| || (\ (          | |      | |   | || |   ) || (        | | \_  )| (      | | \   |
        | (_\ \ || ) \ \__       | (____/\| (___) || (__/  )| (____/\  | (___) || (____/\| )  \  |
        (____\/_)|/   \__/       (_______/(_______)(______/ (_______/  (_______)(_______/|/    )_)
        <rst>"""
        )
    )

    list_options()

    # Get option
    option: str = get_option()

    # Get QR-Code data
    qr_code_data: str = get_qr_code_data(option=option)

    # TODO: Get QR-Code settings

    # Get the output path for the image
    file_path: str = f"./{input('\nEnter the file path for the qrcode: ')}"

    # Create path if it does not exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Write QR-Code
    create_qr_code(data=qr_code_data, file_path=file_path)


if __name__ == "__main__":
    main()
