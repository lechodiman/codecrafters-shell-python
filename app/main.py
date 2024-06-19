import os
import sys
import subprocess


def find_executable(cmd: str) -> str:
    path = os.environ.get('PATH')
    executable_dirs = path.split(':')

    for dir in executable_dirs:
        if os.path.exists(f"{dir}/{cmd}"):
            return f"{dir}/{cmd}"


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        input_command = input()
        cmd, *args = input_command.split(' ')

        command_types = {
            "echo": "builtin",
            "exit": "builtin",
            "type": "builtin",
            "pwd": "builtin",
            "cd": "builtin"
        }

        if cmd == "echo":
            sys.stdout.write(' '.join(args) + '\n')
        elif cmd == "exit":
            sys.exit(0)
        elif cmd == "pwd":
            sys.stdout.write(f"{os.getcwd()}\n")
        elif cmd == "cd":
            new_dir = args[0] if args else os.environ.get('HOME')
            new_dir_exists = os.path.exists(new_dir)

            if new_dir_exists:
                os.chdir(new_dir)
            else:
                sys.stdout.write(f"cd {new_dir}: no such file or directory\n")

        elif cmd == "type":
            arg = args[0] if args else ""
            cmd_type = command_types.get(arg, "nonexistent")

            if cmd_type == "builtin":
                sys.stdout.write(f"{arg} is a shell builtin\n")
            else:
                path = find_executable(arg)

                if path:
                    sys.stdout.write(f"{arg} is {path}\n")
                else:
                    sys.stdout.write(f"{arg}: not found\n")
        else:
            path = find_executable(cmd)

            if not path:
                sys.stdout.write(f"{input_command}: command not found\n")
            else:
                subprocess.run([cmd] + args)


if __name__ == "__main__":
    main()
