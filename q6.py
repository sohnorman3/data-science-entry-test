def find_first_negative(lst):
    """
    Task 1
    - Create a function that finds the first negative number in a list (lst).
    - Return the first negative number if found, otherwise return "No negatives".
    - Use a while loop to implement this.
    """
    index = 0
    while index < len(lst): #as long as the index is not longer then the lenght of the index  Execute below.
        if lst[index] < 0: #check each index when occurrence of  number is lesser than 0. Negative number. run next line.
            return lst[index]  # Return the first negative number found
        index += 1  # add 1 to the index to run the next in line index
    return "No negatives"  # Return if no negative number is found



# Task 2
# Invoke the function "find_first_negative" using the following scenario:
# - [3, 5, -1, 7, -2, 8]
# - [2, 10, 7, 0]

# Test cases
print(find_first_negative([3, 5, -1, 7, -2, 8]))  # Expected output: -1, when index of first negative is found. Print value.
print(find_first_negative([2, 10, 7, 0]))         # Expected output: No negatives is found in the lst