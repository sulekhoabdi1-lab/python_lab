from utils import square, is_even, celsius_to_fahrenheit, greet

def main():
    # Test the new greeting feature
    print(greet("Developer"))
    
    user_input = input("Enter a number: ")
    try:
        num = float(user_input)
        
        # Display results
        print(f"Square of {num}: {square(num)}")
        
        # Check even/odd only if it's a whole number
        if num.is_integer():
            print(f"Is {int(num)} even?: {is_even(int(num))}")
        else:
            print(f"Is {num} even?: N/A (decimal number)")
            
        print(f"Fahrenheit equivalent ({num}°C): {celsius_to_fahrenheit(num)}°F")
        
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
