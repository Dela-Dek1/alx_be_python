# global concersion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# conversion functions
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User Interaction
def main():
    """Main function to handle user input and conversion."""

    try:
        temp_input = input("Enter the temperature: ").strip()
        if temp_input[-1].upper() == "F":
            try:
                fahrenheit = float(temp_input[:-1])
                celsius = convert_to_celsius(fahrenheit)
                print(f"{fahrenheit}F is {celsius:.2f}C")

            except ValueError:
                raise ValueError("Invalid temperature. Please enter a numeric value.")

        elif temp_input[-1].upper() == "C":
            try:
                celsius = float(temp_input[:-1])
                fahrenheit = convert_to_fahrenheit(celsius)
                print(f"{celsius}C is {fahrenheit:.2f}F")
            except ValueError:
                raise ValueError("Invalid temperature. Please enter a numeric value.")

        else:
            raise ValueError("Invalid temperature. Please specify the unit as 'C' or 'F'.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

