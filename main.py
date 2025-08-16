import qrcode  # type: ignore
from qrcode import QRCode
from qrcode.image.pil import PilImage  # type: ignore


def create_qr_code(data: str, file_path: str) -> None:
    # Create a QR code object
    qr: QRCode = QRCode(  # type: ignore
        version=1,  # Increased version for a larger QR Code
        error_correction=qrcode.ERROR_CORRECT_H,  # Controls the error correction used
        box_size=15,  # Increased box size for larger individual boxes
        border=2,  # Controls how many boxes thick the border should be
    )

    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img: PilImage = qr.make_image(fill_color="black", back_color="white")  # type: ignore

    # Save the image to a file
    img.save(file_path)  # type: ignore


def main() -> None:
    create_qr_code("https://example.com", "example.png")


if __name__ == "__main__":
    main()
