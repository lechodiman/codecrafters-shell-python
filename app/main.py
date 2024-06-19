import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        input_command = input()

        if input_command == "exit 0":
            sys.exit(0)

        sys.stdout.write(f"{input_command}: command not found\n")


if __name__ == "__main__":
    main()
