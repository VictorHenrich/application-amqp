from typing import Optional, Mapping, Union
from pathlib import Path
from dotenv import dotenv_values


class EnvUtil:
    @staticmethod
    def get_values(
        file_path: Optional[Union[str, Path]] = None
    ) -> Mapping[str, Optional[str]]:
        path: Path

        if file_path:
            path = Path(file_path)

        else:
            path = list(Path.cwd().glob("**/*.env"))[0]

        if not path.exists():
            raise Exception("Path not found!")

        return dotenv_values(str(path))
