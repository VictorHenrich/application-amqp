from typing import (
    Union,
    Optional,
    TypeAlias,
    Coroutine,
    Awaitable
)
from abc import ABC, abstractmethod
import asyncio
from colorama import Fore, Style

OptionalString: TypeAlias = Optional[str]


class Task(ABC):
    def __init__(
        self,
        name: str,
        shortname: OptionalString,
        description: OptionalString,
        debug: bool
    ) -> None:
        self.__name: str = name
        self.__shortname: OptionalString = shortname
        self.__description: OptionalString = description
        self.__debug: bool = debug
    
    @property
    def name(self) -> str:
        return self.__name

    @property
    def shortname(self) -> OptionalString:
        return self.__shortname

    @property
    def description(self) -> OptionalString:
        return self.__description

    @property
    def debug(self) -> bool:
        return self.__debug

    @abstractmethod
    def run(self) -> Union[None, Awaitable[None]]:
        pass

    def __reset_print(self) -> None:
        print(Style.RESET_ALL, Fore.RESET)

    def __success_print(self) -> None:
        print(Fore.LIGHTGREEN_EX, Style.BRIGHT, Style.DIM)
        print(f'### SUCCESS IN TASK {self.__name.upper()}\n')

        self.__reset_print()

    def __initial_print(self) -> None:
        print(Fore.LIGHTBLUE_EX, Style.BRIGHT, Style.DIM)
        print(f'### RUNNING TASK {self.__name.upper()}\n')

        self.__reset_print()

    def __error_print(self, error: BaseException) -> None:
        print(Fore.LIGHTRED_EX, Style.BRIGHT, Style.DIM)
        print(f"### ERROR IN TASK {self.__name.upper()}\n\n")
        print(f"### TRACEBACK: {error}")

        self.__reset_print()

    def execute(self, args: None = None) -> None:
        result: Optional[Coroutine] = self.run()

        if type(result) is Coroutine:
            asyncio.run(result)