"""
Subprocess Module Tutorial - Educational Examples
==================================================
This module demonstrates various ways to execute Linux/Unix system commands
using Python's subprocess module with proper error handling and argument passing.

NOTE: This code is for educational purposes only, not production use.
"""

import subprocess
import sys
from typing import Optional


# ==============================================================================
# SECTION 1: Basic Command Execution
# ==============================================================================


def example_basic_run():
    """
    Demonstrates the most basic subprocess.run() usage.
    subprocess.run() is the recommended high-level interface (Python 3.5+)
    """
    print("=" * 70)
    print("EXAMPLE 1: Basic Command Execution")
    print("=" * 70)

    # Simple command - just runs and returns a CompletedProcess object
    print("\n[Running: ls -l]")
    result = subprocess.run(["ls", "-l"])
    print(f"Return code: {result.returncode}")
    print("Note: Output went directly to console (not captured)\n")


def example_capture_output():
    """
    Demonstrates capturing stdout and stderr from commands.
    """
    print("=" * 70)
    print("EXAMPLE 2: Capturing Command Output")
    print("=" * 70)

    # Capture output as text (string) instead of bytes
    print("\n[Running: echo 'Hello from subprocess']")
    result = subprocess.run(
        ["echo", "Hello from subprocess"],
        capture_output=True,  # Captures both stdout and stderr
        text=True,  # Returns strings instead of bytes
    )

    print(f"Return code: {result.returncode}")
    print(f"Standard output: {result.stdout.strip()}")
    print(f"Standard error: {result.stderr.strip()}")
    print()


# ==============================================================================
# SECTION 2: Command Arguments and Safety
# ==============================================================================


def example_command_arguments():
    """
    Demonstrates safe vs unsafe ways to pass command arguments.
    IMPORTANT: Always use list format to prevent shell injection!
    """
    print("=" * 70)
    print("EXAMPLE 3: Command Arguments (Safe Method)")
    print("=" * 70)

    # SAFE: Pass command and arguments as a list
    directory = "/etc"
    print(f"\n[Running: ls -lh {directory}]")
    result = subprocess.run(
        ["ls", "-lh", directory],  # Each argument is a separate list item
        capture_output=True,
        text=True,
    )

    print("First 5 lines of output:")
    lines = result.stdout.split("\n")[:5]
    for line in lines:
        print(f"  {line}")
    print()


def example_shell_mode():
    """
    Demonstrates shell=True (useful but dangerous if not careful).
    Use only when you need shell features like pipes, wildcards, etc.
    """
    print("=" * 70)
    print("EXAMPLE 4: Using Shell Mode (Use with Caution!)")
    print("=" * 70)

    # With shell=True, you can use shell features like pipes
    print("\n[Running: ls -l | head -5]")
    result = subprocess.run(
        "ls -l | head -5",  # String instead of list when shell=True
        shell=True,
        capture_output=True,
        text=True,
    )

    print("Output:")
    print(result.stdout)

    print("WARNING: shell=True can be dangerous with user input!")
    print("Only use with trusted, sanitized input or hardcoded commands.\n")


# ==============================================================================
# SECTION 3: Error Handling
# ==============================================================================


def example_error_handling():
    """
    Demonstrates comprehensive error handling for subprocess operations.
    """
    print("=" * 70)
    print("EXAMPLE 5: Error Handling")
    print("=" * 70)

    # Test Case 1: Command that doesn't exist
    print("\n[Test 1: Command not found]")
    try:
        result = subprocess.run(
            ["this_command_does_not_exist"],
            capture_output=True,
            text=True,
            check=True,  # Raises CalledProcessError if return code != 0
        )
    except FileNotFoundError as e:
        print(f"[ERROR] FileNotFoundError: Command not found")
        print(f"   Details: {e}\n")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] CalledProcessError: Command failed with code {e.returncode}")

    # Test Case 2: Command that fails (non-zero exit code)
    print("[Test 2: Command with error exit code]")
    try:
        result = subprocess.run(
            ["ls", "/this/directory/does/not/exist"],
            capture_output=True,
            text=True,
            check=True,  # This will raise exception on non-zero exit
        )
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Command failed with return code: {e.returncode}")
        print(f"   Error output: {e.stderr.strip()}\n")
    except FileNotFoundError as e:
        print(f"[ERROR] FileNotFoundError: {e}\n")

    # Test Case 3: Handling errors without exception (check=False)
    print("[Test 3: Handling errors without exceptions]")
    result = subprocess.run(
        ["ls", "/nonexistent"],
        capture_output=True,
        text=True,
        check=False,  # Don't raise exception, just return result
    )

    if result.returncode != 0:
        print(f"[WARNING] Command failed with code {result.returncode}")
        print(f"   Error: {result.stderr.strip()}")
    else:
        print(f"[SUCCESS] Command succeeded")
    print()


# ==============================================================================
# SECTION 4: Timeout and Process Control
# ==============================================================================


def example_timeout():
    """
    Demonstrates timeout functionality to prevent hanging processes.
    """
    print("=" * 70)
    print("EXAMPLE 6: Timeout Handling")
    print("=" * 70)

    print("\n[Running: sleep 2 with 5 second timeout - should succeed]")
    try:
        result = subprocess.run(
            ["sleep", "2"],
            timeout=5,  # Kill process after 5 seconds
            capture_output=True,
            text=True,
        )
        print(f"[SUCCESS] Command completed (return code: {result.returncode})\n")
    except subprocess.TimeoutExpired as e:
        print(f"[ERROR] Command timed out after {e.timeout} seconds\n")

    print("[Running: sleep 10 with 2 second timeout - should timeout]")
    try:
        result = subprocess.run(["sleep", "10"], timeout=2, capture_output=True, text=True)
        print(f"[SUCCESS] Command completed")
    except subprocess.TimeoutExpired as e:
        print(f"[ERROR] Command timed out after {e.timeout} seconds")
        print(f"   Command was: {e.cmd}\n")


# ==============================================================================
# SECTION 5: Working with Input/Output
# ==============================================================================


def example_stdin_input():
    """
    Demonstrates passing input to commands via stdin.
    """
    print("=" * 70)
    print("EXAMPLE 7: Passing Input to Commands")
    print("=" * 70)

    print("\n[Piping text to 'grep' command]")
    input_text = """apple
banana
cherry
date
elderberry"""

    result = subprocess.run(
        ["grep", "berry"],
        input=input_text,  # Pass this as stdin
        capture_output=True,
        text=True,
    )

    print(f"Input text had {len(input_text.split())} lines")
    print(f"Grep found: {result.stdout.strip()}\n")


def example_piping_commands():
    """
    Demonstrates piping output from one command to another.
    """
    print("=" * 70)
    print("EXAMPLE 8: Piping Between Commands")
    print("=" * 70)

    print("\n[Running: ps aux | grep python]")

    # Method 1: Using shell=True (simpler but less safe)
    result = subprocess.run("ps aux | grep python | head -5", shell=True, capture_output=True, text=True)
    print("Output (using shell):")
    print(result.stdout)

    # Method 2: Piping manually (safer, more complex)
    print("\n[Same thing without shell=True]")
    ps_process = subprocess.run(["ps", "aux"], capture_output=True, text=True)

    grep_process = subprocess.run(
        ["grep", "python"],
        input=ps_process.stdout,  # Use output of ps as input to grep
        capture_output=True,
        text=True,
    )

    head_process = subprocess.run(["head", "-5"], input=grep_process.stdout, capture_output=True, text=True)

    print("Output (manual piping):")
    print(head_process.stdout)


# ==============================================================================
# SECTION 6: Environment Variables and Working Directory
# ==============================================================================


def example_environment_and_cwd():
    """
    Demonstrates running commands with custom environment and working directory.
    """
    print("=" * 70)
    print("EXAMPLE 9: Custom Environment and Working Directory")
    print("=" * 70)

    import os

    # Run command with custom environment variable
    print("\n[Running command with custom environment variable]")
    custom_env = os.environ.copy()
    custom_env["MY_CUSTOM_VAR"] = "Hello from custom environment"

    result = subprocess.run(["bash", "-c", "echo $MY_CUSTOM_VAR"], env=custom_env, capture_output=True, text=True)
    print(f"Output: {result.stdout.strip()}")

    # Run command in different directory
    print("\n[Running 'pwd' in /tmp directory]")
    result = subprocess.run(
        ["pwd"],
        cwd="/tmp",  # Change working directory
        capture_output=True,
        text=True,
    )
    print(f"Working directory was: {result.stdout.strip()}\n")


# ==============================================================================
# SECTION 7: Real-World Helper Function
# ==============================================================================


def run_command_safe(
    command: list[str], timeout: Optional[int] = None, input_data: Optional[str] = None
) -> tuple[bool, str, int]:
    """
    A robust helper function for running commands with comprehensive error handling.

    Args:
        command: List of command and arguments (e.g., ["ls", "-l", "/tmp"])
        timeout: Maximum seconds to wait (None = no timeout)
        input_data: Data to pass to stdin (optional)

    Returns:
        Tuple of (success: bool, output: str, return_code: int)

    Examples:
        >>> success, output, code = run_command_safe(["ls", "-l"])
        >>> success, output, code = run_command_safe(["sleep", "5"], timeout=2)
    """
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=timeout,
            input=input_data,
            check=False,  # We'll check return code manually
        )

        # Return both stdout and stderr combined
        output = result.stdout
        if result.stderr:
            output += f"\nSTDERR:\n{result.stderr}"

        success = result.returncode == 0
        return success, output.strip(), result.returncode

    except FileNotFoundError:
        return False, f"Command not found: {command[0]}", -1

    except subprocess.TimeoutExpired:
        return False, f"Command timed out after {timeout} seconds", -1

    except Exception as e:
        return False, f"Unexpected error: {str(e)}", -1


def example_helper_function():
    """
    Demonstrates using the reusable helper function.
    """
    print("=" * 70)
    print("EXAMPLE 10: Using Helper Function")
    print("=" * 70)

    # Test 1: Successful command
    print("\n[Test 1: Successful command]")
    success, output, code = run_command_safe(["echo", "Hello, World!"])
    print(f"Success: {success} | Return Code: {code}")
    print(f"Output: {output}\n")

    # Test 2: Failed command
    print("[Test 2: Failed command]")
    success, output, code = run_command_safe(["ls", "/nonexistent"])
    print(f"Success: {success} | Return Code: {code}")
    print(f"Output: {output}\n")

    # Test 3: Command with timeout
    print("[Test 3: Command with timeout]")
    success, output, code = run_command_safe(["sleep", "5"], timeout=1)
    print(f"Success: {success} | Return Code: {code}")
    print(f"Output: {output}\n")

    # Test 4: Command not found
    print("[Test 4: Command not found]")
    success, output, code = run_command_safe(["nonexistent_cmd"])
    print(f"Success: {success} | Return Code: {code}")
    print(f"Output: {output}\n")


# ==============================================================================
# SECTION 8: Security Considerations
# ==============================================================================


def example_security_considerations():
    """
    Demonstrates security best practices and common pitfalls.
    """
    print("=" * 70)
    print("EXAMPLE 11: Security Considerations")
    print("=" * 70)

    print("\n[SAFE] Using list format with separate arguments")
    user_input = "/etc/passwd"
    result = subprocess.run(["cat", user_input], capture_output=True, text=True)
    print(f"Command: ['cat', '{user_input}']")
    print(f"First line: {result.stdout.split(chr(10))[0] if result.returncode == 0 else 'Failed'}\n")

    print("[DANGEROUS] Using shell=True with user input")
    print("   NEVER DO THIS:")
    print(f"   subprocess.run(f'cat {{user_input}}', shell=True)")
    print("   If user_input is '; rm -rf /', it would execute!")
    print()

    print("[BEST PRACTICE] Always use list format instead of shell=True")
    print("   This prevents shell injection attacks entirely")
    print("   Example: subprocess.run(['cat', user_input], ...)")
    print()


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================


def main():
    """
    Main function to run all examples.
    """
    print("\n")
    print("█" * 70)
    print("█" + " " * 68 + "█")
    print("█" + "  PYTHON SUBPROCESS MODULE - COMPREHENSIVE TUTORIAL".center(68) + "█")
    print("█" + "  Educational Examples Only - Not for Production".center(68) + "█")
    print("█" + " " * 68 + "█")
    print("█" * 70)
    print("\n")

    examples = [
        ("Basic Execution", example_basic_run),
        ("Capture Output", example_capture_output),
        ("Command Arguments", example_command_arguments),
        ("Shell Mode", example_shell_mode),
        ("Error Handling", example_error_handling),
        ("Timeout", example_timeout),
        ("Input/Output", example_stdin_input),
        ("Piping Commands", example_piping_commands),
        ("Environment & CWD", example_environment_and_cwd),
        ("Helper Function", example_helper_function),
        ("Security", example_security_considerations),
    ]

    for i, (name, func) in enumerate(examples, 1):
        try:
            func()
            input(f"\nPress Enter to continue to next example... ")
        except KeyboardInterrupt:
            print("\n\n[WARNING] Tutorial interrupted by user.")
            sys.exit(0)
        except Exception as e:
            print(f"\n[ERROR] Example '{name}' raised an exception: {e}")
            input("Press Enter to continue... ")

    print("\n" + "=" * 70)
    print("[SUCCESS] Tutorial Complete!")
    print("=" * 70)
    print("\nKey Takeaways:")
    print("1. Use subprocess.run() for most tasks")
    print("2. Pass commands as lists, not strings (safer)")
    print("3. Use capture_output=True and text=True to get string output")
    print("4. Handle errors with try/except for CalledProcessError and FileNotFoundError")
    print("5. Use timeout parameter to prevent hanging processes")
    print("6. Avoid shell=True unless necessary, and never with user input")
    print("\nFor more info: https://docs.python.org/3/library/subprocess.html\n")


if __name__ == "__main__":
    main()
