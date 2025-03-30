def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """

    def swap(x, y):
        """
        Task 1
        - Create a function that would swap the value of x and y using only x and y as variables.
        - x and y must be numeric.
        - Return -1 if x and y is not numeric, and
        - print the swapped values if both x and y are numeric.
        """

        if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
            #compare x & y  is int or float. If either X or Y is false statement will be true "not" and run the next line.

            return -1
        #return -1

        x, y = y, x  # Swapping values, when IF function above is not met
        print("Swapped values:", x, y) #print the value of X & Y with their value swapped


# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
# Get user input
try:
    x = float(input("Enter first number (x): "))
    y = float(input("Enter second number (y): "))
    # Check input that only numeric is entered. If false, except message will be trigger and exit.
    swap(x, y)
    print("Swapped values:", x, y) # Added  print statement as a check to ensure the swap is done
except ValueError:
    print("Invalid input. Please enter numeric values.")