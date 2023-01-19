from typing import Mapping, TypeAlias, Any, Sequence
from argparse import ArgumentParser, _SubParsersAction
from multiprocessing import Process
import sys

from .icommand import ICommand


ITask: TypeAlias = ICommand[Any]

TasksMapping: TypeAlias = Mapping[str, ITask]


class TaskManager:
    def __init__(
        self, 
        name: str,
        subparser: _SubParsersAction
    ) -> None:
        self.__name: str = name

        self.__argument: ArgumentParser = subparser.add_parser(
            name
        )

        self.__tasks: TasksMapping = {}

    @property
    def name(self) -> str:
        return self.__name

    def add_task(self, task: ITask) -> None:
        self.__tasks[task.name] = task

    def execute(self, args: Sequence[str]) -> None:
        handle_args: Sequence[str] = [a.upper() for a in args]

        processes: Sequence[Process] = [
            Process(target=task.execute, args=(None, ))
            for task_name, task in self.__tasks.items()
            if task_name.upper() in handle_args
        ]

        if not processes:
            self.__argument.print_help()
            
            sys.exit()

        [process.start() for process in processes]
        [process.join() for process in processes]

