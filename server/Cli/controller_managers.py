from typing import (
    Union, 
    Tuple, 
    TypeAlias, 
    Mapping,
    Optional,
    Any,
    Sequence
)
from argparse import ArgumentParser, _SubParsersAction, Namespace
from .icommand import ICommand

from .task_manager import TaskManager
from .task import Task


SubParsers: TypeAlias = _SubParsersAction[ArgumentParser]
ITask: TypeAlias = ICommand[Any]
ITaskManager: TypeAlias = ICommand[Sequence[str]]



class ControllerManagers:
    def __init__(
        self,
        name: str,
        version: Union[float, str], 
        description: str = "",
        usage: str = ""
    ) -> None:
        argument, subparsers = self.__create_config_argument(
            name,
            version,
            description,
            usage
        )

        self.__argument: ArgumentParser = argument
        self.__subparsers: SubParsers = subparsers
        self.__managers: Mapping[str, ITaskManager] = {}

    def __create_config_argument(
        self,
        name: str,
        version: Union[float, str], 
        description: str,
        usage: str
    ) -> Tuple[ArgumentParser, SubParsers]:

        argument: ArgumentParser = ArgumentParser(
            prog=name,
            description=description,
            usage=usage
        )

        subparsers: SubParsers = argument.add_subparsers(
            dest="module",
            description="These modules are the task managers created in the system.",
            title="Task Managers",
            required=True
        )

        argument.add_argument(
            '-v',
            '--version',
            action="version",
            version=f"{name} {version}"
        )

        return argument, subparsers

    def add_task(
        self,
        name: str,
        task_manager_name: str,
        shortname: Optional[str] = None,
        description: Optional[str] = None,
        debug: bool = False
    ):
        def wrapper(cls: Task):
            task: ITask = cls(
                name,
                shortname,
                description,
                debug
            )

            task_manager: TaskManager = [
                manager
                for manager_name, manager in self.__managers.items()
                if manager_name.upper() == task_manager_name.upper()
            ][0]

            task_manager.add_task(task)

            return cls

        return wrapper

    def execute(self) -> None:
        namespaces: Namespace = self.__argument.parse_args()

        try:
            task_manager: ITaskManager = [
                manager
                for key, manager in self.__managers.items()
                if key == namespaces.module
            ][0]

        except IndexError:
            self.__argument.print_help()

        else:
            args: Sequence[str] = [
                key
                for key, value in namespaces.__dict__.items()
                if value is True
            ]

            task_manager.execute(args)