from typing import Mapping
from pathlib import Path


__PATH_DRIVES__: Path = Path.cwd() / "drives" / "users"

__MIME_TYPES__: Mapping[str, str] = {
    "txt": "plain/txt",
    "pdf": "application/pdf",
    "html": "plain/html",
}
