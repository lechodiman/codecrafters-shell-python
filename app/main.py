from abc import ABC, abstractmethod
import os
import sys
import subprocess


def find_executable(cmd: str) -> str:
    path = os.environ.get('PATH')
    executable_dirs = path.split(':')

    for dir in executable_dirs:
        if os.path.exists(f"{dir}/{cmd}"):
            return f"{dir}/{cmd}"


class Command(ABC):
    @abstractmethod
    def execute(self, cmd, *args):
        pass


class EchoCommand(Command):
    def execute(self, cmd, *args):
        sys.stdout.write(' '.join(args) + '\n')


class ExitCommand(Command):
    def execute(self, cmd, *args):
        sys.exit(0)


class PwdCommand(Command):
    def execute(self, cmd, *args):
        sys.stdout.write(f"{os.getcwd()}\n")


class CdCommand(Command):
    def execute(self, cmd, *args):
        new_dir = args[0] if args else os.environ.get('HOME')
        new_dir_exists = os.path.exists(new_dir)

        if new_dir_exists:
            os.chdir(new_dir)
        else:
            sys.stdout.write(f"cd: {new_dir}: No such file or directory\n")


class TypeCommand(Command):
    def __init__(self, builtin_commands):
        self.builtin_commands = builtin_commands

    def execute(self, cmd, *args):
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
    def execute(self, cmd, *args):
        path = find_executable(cmd)

        if not path:
            sys.stdout.write(f"{cmd}: command not found\n")
        else:
            subprocess.run([cmd] + list(args))


def main():
    builtin_commands = {
        "echo", "exit", "type", "pwd", "cd"
    }

    command_types = {
        "echo": EchoCommand(),
        "exit": ExitCommand(),
        "type": TypeCommand(builtin_commands),
        "pwd": PwdCommand(),
        "cd": CdCommand()
    }

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        input_command = input()
        cmd, *args = input_command.split(' ')

        command = command_types.get(cmd, ExternalCommand())
        command.execute(*[cmd] + args)


if __name__ == "__main__":
    main()
