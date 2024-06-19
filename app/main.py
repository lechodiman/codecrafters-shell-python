import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        input_command = input()

        cmd, *args = input_command.split(' ')

        if cmd == "echo":
            sys.stdout.write(' '.join(args) + '\n')
        elif input_command == "exit 0":
            sys.exit(0)
        else:
            sys.stdout.write(f"{input_command}: command not found\n")


if __name__ == "__main__":
    main()
