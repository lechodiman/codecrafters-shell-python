import sys


def main():
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    user_input = input()

    sys.stdout.write(f"{user_input}: command not found\n")


if __name__ == "__main__":
    main()
