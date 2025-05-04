import sys  # Import sys to use sys.exit for cleaner error handling

"""
Reads item prices from an input file (Receipt.txt), calculates the
grand total, and writes the total to an output file (GrandTotal.txt).
"""

# --- Configuration: Define Constant Variables for Filenames ---
INPUT_FILENAME = "Receipt.txt"
OUTPUT_FILENAME = "GrandTotal.txt"

# --- Main Logic ---
grand_total = 0

# --- Read Input File and Calculate Total ---
try:
    print(f"Attempting to read file: {INPUT_FILENAME}")
    # Use 'with' statement for safe file handling (automatically closes file)
    with open(INPUT_FILENAME, "r") as infile:
        # Read each line from the input file
        for line_num, line in enumerate(
            infile, 1
        ):  # Start line numbering at 1 for messages
            # Remove leading/trailing whitespace (like newline characters)
            cleaned_line = line.strip()

            # Skip empty lines
            if not cleaned_line:
                continue

            # Split the line into parts based on whitespace
            parts = cleaned_line.split()

            # Expecting two parts: item name and price
            if len(parts) == 2:
                item_name = parts[0]
                price_str = parts[1]

                # Try to convert the price part to an integer
                try:
                    price = int(price_str)
                    grand_total += price  # Add the price to the running total
                except ValueError:
                    # Handle cases where the second part is not a valid number
                    print(
                        f"Warning: Invalid price format on line {line_num} in {INPUT_FILENAME}: '{price_str}'. Skipping line."
                    )
            else:
                # Handle lines that don't have exactly two parts
                print(
                    f"Warning: Malformed line {line_num} in {INPUT_FILENAME}: '{cleaned_line}'. Skipping line."
                )

    print(f"Finished reading {INPUT_FILENAME}. Calculated total: {grand_total}")

except FileNotFoundError:
    print(f"Error: Input file '{INPUT_FILENAME}' not found in the current directory.")
    print(
        "Please make sure the file exists and the script is run from the correct directory."
    )
    sys.exit(1)  # Exit the script with an error code
except Exception as e:
    # Catch other potential file reading errors
    print(f"An unexpected error occurred while reading {INPUT_FILENAME}: {e}")
    sys.exit(1)  # Exit the script with an error code


# --- Format the Output String ---
# Use an f-string for easy formatting, incorporating the calculated total
output_string = f"The grand total of {INPUT_FILENAME} is ${grand_total}"


# --- Write the Grand Total to the Output File ---
try:
    print(f"Attempting to write to file: {OUTPUT_FILENAME}")
    # Open the output file in write mode ('w')
    # This will create the file if it doesn't exist, or overwrite it if it does
    with open(OUTPUT_FILENAME, "w") as outfile:
        outfile.write(output_string + "\n")  # Add a newline for better file formatting

    print(f"Successfully wrote grand total to {OUTPUT_FILENAME}.")

except Exception as e:
    # Catch potential file writing errors
    print(f"An error occurred while writing to {OUTPUT_FILENAME}: {e}")
    sys.exit(1)  # Exit the script with an error code

print("Script completed successfully.")
