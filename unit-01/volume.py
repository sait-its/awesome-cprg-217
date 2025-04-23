# volume.py
# Calculates the volume of a cylinder based on user input.

import math  # Import the math module to use math.pi


def calculate_cylinder_volume(diameter, length):
    """Calculates the volume of a cylinder."""
    if diameter <= 0 or length <= 0:
        raise ValueError("Diameter and length must be positive numbers.")
    radius = diameter / 2
    volume = math.pi * (radius**2) * length
    return volume


def main():
    """Main function to run the volume calculation loop."""
    print("Cylinder Volume Calculator")
    print("Enter 'quit' at any time to exit.")
    print("-" * 30)

    while True:
        # --- User Input ---
        diameter_input = input("Enter the diameter of the cylinder (cm): ")
        # Check for exit condition
        if diameter_input.lower() == "quit":
            break

        length_input = input("Enter the length (height) of the cylinder (cm): ")
        # Check for exit condition
        if length_input.lower() == "quit":
            break

        # --- Error Handling and Data Type Conversion ---
        try:
            # Convert input strings to floating-point numbers (variable data types)
            diameter_cm = float(diameter_input)
            length_cm = float(length_input)

            # --- Calculation ---
            # Call the function to calculate volume, handling potential value errors
            volume_cm3 = calculate_cylinder_volume(diameter_cm, length_cm)

            # --- Output ---
            # Return the result in the specified format, rounding volume to 2 decimal places
            print(
                f"\nThe volume of a cylinder with a {diameter_cm} cm diameter and {length_cm} cm length is {volume_cm3:.2f} cm3.\n"
            )

        except ValueError as e:
            # Handle cases where input is not a valid number or not positive
            print(
                f"Error: Invalid input. {e}. Please enter numeric values greater than zero."
            )
            print("-" * 30)
            continue  # Skip to the next iteration of the loop

        print("-" * 30)  # Separator for the next calculation

    print("\nExiting Cylinder Volume Calculator. Goodbye!")


# --- Script Execution ---
if __name__ == "__main__":
    main()
