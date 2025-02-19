
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    while True:
        try:
            temperature = float(input("Enter the temperature to convert: "))
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F):").strip().upper()
        
            if unit == "C":
                converted = convert_to_fahrenheit(temperature)
                print(f"{temperature}°C is equivalent to {converted:.2f}°F.")

            elif unit == "F":
                converted = convert_to_celsius(temperature)
                print(f"{temperature}°F is equivalent to {converted:.2f}°C.") 
        
            else:
                print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
            exit_choice = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
            if exit_choice == "no":
                print("Goodbye!")
                break


        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")

    

     

if __name__ == "__main__":
    main()

