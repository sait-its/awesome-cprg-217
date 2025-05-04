# This example demonstrates various file operations in Python
# It shows different methods to read and write both text and binary files
# Using pathlib for modern, cross-platform path handling

from pathlib import Path


def main():
    # Create a Path object for our text file
    # Path is more modern and cross-platform compatible than old-style string paths
    text_file_path = Path("sample_text.txt")
    binary_file_path = Path("sample_binary.dat")

    # =============== TEXT FILE OPERATIONS ===============

    # --- Example 1: Writing to a text file using context manager (recommended way) ---
    # The 'with' statement ensures the file is properly closed after we're done
    with open(text_file_path, "w", encoding="utf-8") as file:
        file.write("Hello, Python learners!\n")
        file.write("This is line 2 of our text file.\n")

    # --- Example 2: Reading from a text file using context manager ---
    print("\n=== Reading text file with context manager ===")
    with open(text_file_path, "r", encoding="utf-8") as file:
        # Read entire file content at once
        content = file.read()
        print("File contents:")
        print(content)

    # --- Example 3: Reading text file line by line ---
    print("\n=== Reading text file line by line ===")
    with open(text_file_path, "r", encoding="utf-8") as file:
        for line_number, line in enumerate(file, 1):
            print(f"Line {line_number}: {line.strip()}")

    # --- Example 4: File operations without context manager (not recommended) ---
    # Note: Always remember to close the file when not using context manager
    print("\n=== Writing/Reading without context manager ===")
    file = open(text_file_path, "a", encoding="utf-8")
    file.write("Line added without context manager.\n")
    file.close()  # Important: manually close the file!

    # =============== BINARY FILE OPERATIONS ===============

    # --- Example 5: Writing binary data ---
    # Binary files are useful for non-text data like images, audio, etc.
    print("\n=== Binary file operations ===")
    binary_data = bytes([65, 66, 67, 68, 69])  # ASCII values for 'ABCDE'

    with open(binary_file_path, "wb") as binary_file:
        binary_file.write(binary_data)

    # --- Example 6: Reading binary data ---
    with open(binary_file_path, "rb") as binary_file:
        read_binary = binary_file.read()
        print(f"Binary content as bytes: {read_binary}")
        print(f"Binary content decoded to ASCII: {read_binary.decode('ascii')}")

    # --- Example 7: Using pathlib methods ---
    print("\n=== Pathlib operations ===")
    print(f"Text file exists: {text_file_path.exists()}")
    print(f"Text file size: {text_file_path.stat().st_size} bytes")
    print(f"File suffix: {text_file_path.suffix}")
    print(f"Absolute path: {text_file_path.absolute()}")


if __name__ == "__main__":
    main()
