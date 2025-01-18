
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

# conversion functions
def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACOTR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# User Interaction
whlie True:

    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is it in Celsius (C) or Fahrenheit (F)? ").strip()
        
        if unit == "C":
            converted = convert_to_fahrenheit(temperature)
            print(f"{temperature}C is equivalent to {converted:.2f}F.")

        elif unit == "F":
            converted = convert_to_celsius(temperature)
            print(f"{temperature}F is equivalent to {converted:.2f}C.") 
        
        else:
            print("Invalid unit. Please enter "C" for Celsius or "F" for Fahrenheit.")


    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")

    exit_choice = input("Do you want to convert another temperature? (yes/no): ").strip().lower()
    if exit_choice == "no":
        print("Goodbye!")
        break

     

if __name__ == "__main__":
    main()

