import tempfile
from pathlib import Path
import base64

try:
    import qrcode
    from qrcode.constants import ERROR_CORRECT_L
except ImportError:  # pragma: no cover - optional dependency
    qrcode = None


def create_qr_code(data: str) -> Path:
    """Create QR code image for the given data and return file path."""
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    path = Path(temp.name)
    temp.close()
    if qrcode is None:
        raise RuntimeError(
            "qrcode package is required to generate QR code. Please install it."
        )
    qr = qrcode.QRCode(error_correction=ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(path)
    return path
