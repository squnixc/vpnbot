import tempfile
from pathlib import Path


def create_temp_conf_file(conf: str, filename: str | None = None) -> Path:
    """Create a temporary WireGuard configuration file."""

    temp_dir = Path(tempfile.mkdtemp())
    safe_name = Path(filename).name if filename else "vpn.conf"
    if not safe_name.endswith(".conf"):
        safe_name = f"{safe_name}.conf"
    path = temp_dir / safe_name
    path.write_text(conf)
    return path
