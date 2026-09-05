from utils import square, is_even, celsius_to_fahrenheit

def main():
    # Prompt user for input
    user_input = input("Enter a number: ")
    num = float(user_input)
    
    # Calculate results
    sq = square(num)
    even_status = "even" if is_even(num) else "odd"
    fahrenheit = celsius_to_fahrenheit(num)
    
    # Display results
    print(f"Square: {sq}")
    print(f"The number is {even_status}.")
    print(f"Celsius ({num}°C) in Fahrenheit: {fahrenheit}°F")

if __name__ == "__main__":
    main()
