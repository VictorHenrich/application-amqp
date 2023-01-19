from typing import (
    Generic, 
    TypeVar, 
    Any, 
    Union,
    Optional,
    TypeAlias,
    Coroutine
)
from abc import ABC, abstractmethod
import asyncio
from colorama import Fore, Style


T = TypeVar('T', bound=Union[Any, None])
OptionalString: TypeAlias = Optional[str]


class Task(ABC, Generic[T]):
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
    def run(self, args: T) -> None:
        pass

    def __reset_print(self) -> None:
        print(Style.RESET_ALL, Fore.RESET)

    def __initial_print(self) -> None:
        print(Fore.LIGHTBLUE_EX, Style.BRIGHT, Style.DIM)
        print(f'### SUCCESS IN TASK {self.__name.upper()}\n\n')

        self.__reset_print()

    def __success_print(self) -> None:
        print(Fore.LIGHTBLUE_EX, Style.BRIGHT, Style.DIM)
        print(f'### RUNNING TASK {self.__name.upper()}\n\n')

        self.__reset_print()

    def __error_print(self, error: BaseException) -> None:
        print(Fore.LIGHTRED_EX, Style.BRIGHT, Style.DIM)
        print(f"### ERROR IN TASK {self.__name.upper()}\n\n")
        print(f"### TRACEBACK: {error}")

        self.__reset_print()

    def execute(self, args: T) -> None:
        self.__initial_print()

        try:
            result: Optional[Coroutine] = self.run(args)

            if type(result) is Coroutine:
                asyncio.run(result)


        except BaseException as error:
            self.__error_print(error)

            if self.__debug:
                raise error
        
        else:
            self.__success_print()