import tempfile
from pathlib import Path
from typing import Union

try:
    import qrcode
except ImportError:  # pragma: no cover - optional dependency
    qrcode = None


def create_qr_code(data: str) -> Path:
    """Create QR code image for the given data and return file path."""
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".png")
    path = Path(temp.name)
    temp.close()
    if qrcode:
        img = qrcode.make(data)
        img.save(path)
    else:  # simple fallback
        path.write_text(data)
    return path
