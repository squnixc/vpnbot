import logging
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
    try:
        qr = qrcode.QRCode(error_correction=ERROR_CORRECT_L, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        # Resize to reduce overall dimensions
        img = img.resize((150, 150))
        img.save(path)
    except Exception as e:  # pragma: no cover - optional dependency issues
        logging.exception("QR generation failed: %s", e)
        placeholder = base64.b64decode(
            "iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAIAAAACUFjqAAAAEElEQVR4nGP4jxcwjEpjAwD6Hirkl4HYkQAAAABJRU5ErkJggg=="
        )
        path.write_bytes(placeholder)
    return path
