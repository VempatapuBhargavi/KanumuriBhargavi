import math

def calculate_square_root():
    try:
        num = float(input("Enter a non-negative number: "))
        if num < 0:
            raise ValueError("Number must be non-negative")
        result = math.sqrt(num)
    except ValueError as ve:
        print("Error:", ve)
    except NameError:
        print("Error: Please enter a valid number")
    else:
        print("Square root:", result)
    finally:
        print("Program execution completed.")

calculate_square_root()