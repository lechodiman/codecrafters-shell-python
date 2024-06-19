import sys


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
        }

        if cmd not in command_types:
            sys.stdout.write(f"{input_command}: command not found\n")
            continue

        if cmd == "echo":
            sys.stdout.write(' '.join(args) + '\n')
        elif cmd == "exit":
            sys.exit(0)
        elif cmd == "type":
            arg = args[0] if args else ""
            cmd_type = command_types.get(arg, "nonexistent")

            if cmd_type == "builtin":
                sys.stdout.write(f"{arg} is a shell builtin\n")
            else:
                sys.stdout.write(f"{arg}: not found\n")


if __name__ == "__main__":
    main()
