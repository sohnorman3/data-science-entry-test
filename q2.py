def find_and_replace(lst, find_val, replace_val):
    """
    Task 1
    - Create a function that searches for all occurrences of a value (find_val) in a given list (lst) and replaces them with another value (replace_val).
    - lst must be a list.
    - Return the modified list.
    """
    if not isinstance(lst, list): # isinstance compare if object lst is a list. "Not" function compare if the false run next line.
        raise ValueError("Input must be a list")  #raise is an exception handling if input is not a list

    return [replace_val if item == find_val else item for item in lst]  #  check each item in list with for item in lst, if item is match exactly, replace the find_val with replace_val



# Task 2
# Invoke the function "find_and_replace" using the following scenarios:
# - [1, 2, 3, 4, 2, 2], 2, 5
# - ["apple", "banana", "apple"], "apple", "orange"

# Test Case 1: Replacing 2s with 5s
list1 = [1, 2, 3, 4, 2, 2]
result1 = find_and_replace(list1, 2, 5) # replace all 2 with the value 5 in all the value in the list
print(result1)  # Output: [1, 5, 3, 4, 5, 5]

# Test Case 2: Replacing "apple" with "orange"
list2 = ["apple", "banana", "apple"]
result2 = find_and_replace(list2, "apple", "orange") #replace all apple with Orange in the list. This does not change current orange in the list. 
print(result2)  # Output: ["orange", "banana", "orange"]