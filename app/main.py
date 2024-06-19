import sys
from typing import Dict
from app.commands import CdCommand, Command, EchoCommand, ExitCommand, ExternalCommand, PwdCommand, TypeCommand


def main():
    builtin_commands = {
        "echo", "exit", "type", "pwd", "cd"
    }

    command_types: Dict[str, Command] = {
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
