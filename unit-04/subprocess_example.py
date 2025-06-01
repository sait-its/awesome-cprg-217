#!/usr/bin/env python3

import subprocess
import platform
import sys


def run_command(command):
    """
    Execute a shell command and handle its output safely.

    Args:
        command (list): Command and its arguments as a list
    Returns:
        tuple: (success, output)
    """
    try:
        # subprocess.run() is the recommended way to run commands in Python 3
        # capture_output=True captures both stdout and stderr
        # text=True returns string output instead of bytes
        # check=True will raise CalledProcessError if the command fails
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return True, result.stdout
    except subprocess.CalledProcessError as e:
        return False, f"Command failed with error: {e.stderr}"
    except FileNotFoundError:
        return False, f"Command '{command[0]}' not found"


def main():
    # Determine the operating system to use appropriate commands
    is_windows = platform.system().lower() == "windows"

    # Dictionary of commands for different operating systems
    commands = {
        "list_files": ["dir" if is_windows else "ls", "-la"],
        "current_dir": ["cd" if is_windows else "pwd"],
    }

    print("=== Python Subprocess Example ===\n")

    # Example 1: List files in current directory
    print("1. Listing files in current directory:")
    success, output = run_command(commands["list_files"])
    if success:
        print(f"Success! Output:\n{output}")
    else:
        print(f"Error: {output}")

    print("\n" + "=" * 40 + "\n")

    # Example 2: Show current working directory
    print("2. Getting current working directory:")
    success, output = run_command(commands["current_dir"])
    if success:
        print(f"Success! Current directory is:\n{output}")
    else:
        print(f"Error: {output}")

    # Example 3: Demonstrate error handling with invalid command
    print("\n" + "=" * 40 + "\n")
    print("3. Trying to run an invalid command:")
    success, output = run_command(["this_command_does_not_exist"])
    if success:
        print(f"Success! Output:\n{output}")
    else:
        print(f"Error: {output}")


if __name__ == "__main__":
    main()
