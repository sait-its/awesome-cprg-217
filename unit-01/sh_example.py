#!/usr/bin/env python3

# Import necessary commands from sh module
from sh import ls, pwd, echo, ErrorReturnCode


def run_cmd(command, *args):
    """
    A simple function to run shell commands and handle errors

    Args:
        command: The shell command to run (from sh module)
        *args: Command arguments
    """
    try:
        # Execute the command with any provided arguments
        output = command(*args)
        return str(output)
    except ErrorReturnCode as e:
        return f"Error executing command: {e}"


def main():
    print("=== Simple Shell Command Examples using Python 'sh' module ===\n")

    # Example 1: List files in current directory
    print("1. Listing files in current directory:")
    result = run_cmd(ls)
    print(result)

    print("\n" + "=" * 50 + "\n")

    # Example 2: List files with details
    print("2. Listing files with details (ls -l):")
    result = run_cmd(ls, "-l")
    print(result)

    print("\n" + "=" * 50 + "\n")

    # Example 3: Show current working directory
    print("3. Current working directory:")
    result = run_cmd(pwd)
    print(result)

    print("\n" + "=" * 50 + "\n")

    # Example 4: Echo a message
    print("4. Echo a message:")
    result = run_cmd(echo, "Hello from Python sh module!")
    print(result)


if __name__ == "__main__":
    main()
