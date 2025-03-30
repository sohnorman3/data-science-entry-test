def string_reverse(s):
    """
    Task 1
    - Create a function that reverses a given string (s).
    - s must be a string.
    - Return the reversed string.
    """
    if not isinstance(s, str):  #check if s is a str and if false, run the next line.
        raise ValueError("Input must be a string") # exception raise for input error for the requirement.

    return s[::-1]  # Reverse the string using slicing. [Start,end, step] with [::-1] we are defining default all beginning and default ending with a negative left to right order.



# Task 2
# Invoke the function "string_reverse" using the following scenarios:
# - "Hello World"
# - "Python"

# Test Case 1: Reversing "Hello World"
result1 = string_reverse("Hello World") #define object result1, call function string reverse
print(result1)  # Output: "dlroW olleH"  # print result of result1

# Test Case 2: Reversing "Python"
result2 = string_reverse("Python")   #define object result2, call function string reverse
print(result2)  # Output: "nohtyP" Print result of result2