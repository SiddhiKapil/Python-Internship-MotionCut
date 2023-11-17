def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Welcome to the Temperature Converter!")

    while True:
        try:
            value = float(input("Enter the temperature value: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid numeric value.")

    source_unit = input("Enter the source unit (C for Celsius, F for Fahrenheit): ").upper()
    target_unit = input("Enter the target unit (C for Celsius, F for Fahrenheit): ").upper()

    try:
        if source_unit == 'C' and target_unit == 'F':
            result = celsius_to_fahrenheit(value)
            print(f"\n{value} Celsius is equal to {result:.2f} Fahrenheit.")
        elif source_unit == 'F' and target_unit == 'C':
            result = fahrenheit_to_celsius(value)
            print(f"\n{value} Fahrenheit is equal to {result:.2f} Celsius.")
        elif source_unit == target_unit:
            print("Source and target units are the same. No conversion needed.")
        else:
            print("Unsupported units. Please enter 'C' or 'F'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

