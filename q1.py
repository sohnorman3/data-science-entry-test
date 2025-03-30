def swap_values(x, y):
    """
    Task 1
    - Create a function that swaps the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y are not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    # Check if both x and y are numeric (int or float)
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        # this statement define X & Y has to be an Integer or float = true otherwise this will be false
        # and function compare both X and Y has to be numeric before the statement be set to true
        # Not function invert the condition. Either X and Y is 1 or both false. Not function will process return -1 code

        return -1  # Return -1 if either x or y is not numeric

    # Swap the values of x and y
    x, y = y, x # Swapping values, when IF function above is not met

    # Print the swapped values
    print(f"Swapped values: x = {x}, y = {y}") #print the value of X & Y with their value swapped


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
# Get user input
try:
    x = float(input("Enter first number (x): "))
    y = float(input("Enter second number (y): "))
    # Check input that only numeric is entered. If false, except message will be trigger and exit.
    swap_values(x, y)
    print("Swapped values:", x, y) # Added the print statement as a check to ensure the swap is done
except ValueError:
    print("Invalid input. Please enter numeric values.")