#!/usr/bin/env python3

# Import the argparse module for handling command-line arguments
import argparse


def main():
    # Create an ArgumentParser object
    # description: This text will be displayed in the help message
    parser = argparse.ArgumentParser(
        description="A simple example script demonstrating argparse usage"
    )

    # Add command line arguments
    # add_argument() method defines how a single command-line argument should be parsed
    # Required argument
    parser.add_argument(
        "name",  # Name of the argument
        help="Name to greet",  # Help text for this argument
    )

    # Optional argument with a default value
    parser.add_argument(
        "--greeting",  # Option name
        "-g",  # Short option name
        default="Hello",  # Default value if argument is not provided
        help="Greeting to use",  # Help text for this argument
    )

    # Optional flag (True/False)
    parser.add_argument(
        "--uppercase",  # Option name
        "-u",  # Short option name
        action="store_true",  # This makes it a boolean flag
        help="Display in uppercase",  # Help text for this argument
    )

    # Parse the arguments
    args = parser.parse_args()

    # Create the greeting message
    message = f"{args.greeting}, {args.name}!"

    # Convert to uppercase if the uppercase flag is set
    if args.uppercase:
        message = message.upper()

    # Print the result
    print(message)


if __name__ == "__main__":
    main()
