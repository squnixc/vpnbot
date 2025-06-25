import tempfile
from pathlib import Path


def create_temp_conf_file(conf: str) -> Path:
    """Create a temporary vpn.conf file with provided configuration."""
    temp_dir = Path(tempfile.mkdtemp())
    path = temp_dir / "vpn.conf"
    path.write_text(conf)
    return path
