import tempfile
from pathlib import Path
from typing import Union
import base64

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
        # provide valid PNG placeholder to avoid Telegram IMAGE_PROCESS_FAILED
        placeholder = base64.b64decode(
            "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8z/C/HgAHggJ/P/BdVwAAAABJRU5ErkJggg=="
        )
        path.write_bytes(placeholder)
    return path
