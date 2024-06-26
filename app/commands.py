from abc import ABC, abstractmethod
import os
import sys
import subprocess
from typing import Optional


def find_executable(cmd: str) -> Optional[str]:
    path = os.environ.get('PATH')
    executable_dirs = path.split(':')

    for dir in executable_dirs:
        if os.path.exists(f"{dir}/{cmd}"):
            return f"{dir}/{cmd}"


class Command(ABC):
    @abstractmethod
    def execute(self, cmd: str, *args: str) -> None:
        pass


class EchoCommand(Command):
    def execute(self, cmd: str, *args: str) -> None:
        sys.stdout.write(' '.join(args) + '\n')


class ExitCommand(Command):
    def execute(self, cmd: str, *args: str) -> None:
        sys.exit(0)


class PwdCommand(Command):
    def execute(self, cmd: str, *args: str) -> None:
        sys.stdout.write(f"{os.getcwd()}\n")


class CdCommand(Command):
    def execute(self, cmd: str, *args: str) -> None:
        new_dir = args[0] if args else os.environ.get('HOME')

        if new_dir == "~":
            new_dir = os.environ.get('HOME')

        new_dir_exists = os.path.exists(new_dir)

        if new_dir_exists:
            os.chdir(new_dir)
        else:
            sys.stdout.write(f"cd: {new_dir}: No such file or directory\n")


class TypeCommand(Command):
    def __init__(self, builtin_commands: set[str]):
        self.builtin_commands = builtin_commands

    def execute(self, cmd: str, *args: str) -> None:
        arg = args[0] if args else ""

        if arg in self.builtin_commands:
            sys.stdout.write(f"{arg} is a shell builtin\n")
        else:
            path = find_executable(arg)

            if path:
                sys.stdout.write(f"{arg} is {path}\n")
            else:
                sys.stdout.write(f"{arg}: not found\n")


class ExternalCommand(Command):
    def execute(self, cmd: str, *args: str) -> None:
        path = find_executable(cmd)

        if not path:
            sys.stdout.write(f"{cmd}: command not found\n")
        else:
            subprocess.run([cmd] + list(args))
