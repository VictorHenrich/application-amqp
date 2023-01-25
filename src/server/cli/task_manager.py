from typing import Mapping, TypeAlias, Any, Sequence
from argparse import ArgumentParser, _SubParsersAction
from multiprocessing import Process
import sys

from .icommand import ICommand
from .task import Task


TasksMapping: TypeAlias = Mapping[str, ICommand[Any]]


class TaskManager:
    def __init__(self, name: str, subparser: _SubParsersAction) -> None:
        self.__name: str = name

        self.__argument: ArgumentParser = subparser.add_parser(name)

        self.__tasks: TasksMapping = {}

    @property
    def name(self) -> str:
        return self.__name

    @property
    def tasks(self) -> TasksMapping:
        return self.__tasks

    def add_task(self, task: Task) -> None:
        self.__tasks[task.name] = task

        names: Sequence[str] = [f"--{task.name}"]

        if task.shortname:
            names.append(f"-{task.shortname}")

        self.__argument.add_argument(*names, action="store_true", help=task.description)

    def execute(self, args: Sequence[str]) -> None:
        try:
            handle_args: Sequence[str] = [a.upper() for a in args]

            task: ICommand[None] = [
                task
                for task_name, task in self.__tasks.items()
                if task_name.upper() in handle_args
            ][0]

            task.execute()

        except IndexError:
            self.__argument.print_help()

            sys.exit(0)
