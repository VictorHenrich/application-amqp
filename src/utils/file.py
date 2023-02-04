from typing import IO, Union, TypeAlias, Literal, TextIO, BinaryIO
from pathlib import Path
from io import BytesIO, StringIO


FilePath: TypeAlias = Union[str, Path]
ReadMode: TypeAlias = Literal["rb", "r"]
WriteMode: TypeAlias = Literal["wb", "w"]


class FileUtil:
    @staticmethod
    def read(path: FilePath, mode: ReadMode = "rb") -> IO:
        filepath: Path = Path(path)

        with open(filepath, mode) as file:
            file_content: Union[str, bytes] = file.read()

            if type(file_content) is str:
                return StringIO(file_content)

            if type(file_content) is bytes:
                return BytesIO(file_content)

            else:
                raise Exception("File type is invalid!")

    @staticmethod
    def write(
        path: FilePath, content: Union[str, bytes], mode: WriteMode = "wb"
    ) -> None:
        filepath: Path - Path(path)

        with open(filepath, mode) as file:
            file.write(content)
