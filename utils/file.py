import tempfile
from pathlib import Path


def create_temp_conf_file(conf: str) -> Path:
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".conf")
    path = Path(temp.name)
    temp.close()
    path.write_text(conf)
    return path
