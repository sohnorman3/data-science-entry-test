def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if not (isinstance(num, (int, float)) and isinstance(divisor, (int, float))): # check if num is a numeric and Divisor is numeric. if either is false run next line
        raise ValueError("Both num and divisor must be numeric.") # exception handing of message both num and divisor must be numeric

    return num % divisor == 0  # Return True if num is divisible by divisor. alternatively using return (num / divisor).is_integer() or non decimal



# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3
