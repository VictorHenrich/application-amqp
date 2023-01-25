from typing import Optional
from pathlib import Path

from utils.constants import __PATH_DRIVES__


class MainPathCreationService:
    def execute(self, args: Optional[Path] = None) -> None:
        main_path: Path = Path(__PATH_DRIVES__)

        if not main_path.exists():
            main_path.mkdir(parents=True)
