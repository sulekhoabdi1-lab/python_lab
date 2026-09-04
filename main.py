from utils import square, is_even, celsius_to_fahrenheit

def main():
    try:
        val = float(input("Enter a number: "))
        print(f"Square: {square(val)}")
        print(f"Is Even: {is_even(val)}")
        print(f"Fahrenheit equivalent: {celsius_to_fahrenheit(val)}°F")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
