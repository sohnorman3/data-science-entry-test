def update_dictionary(dct, key, value):
    """
    Task 1
    - Create a function that updates a dictionary (dct) with a new key-value pair.
    - If the key already exists in dct, print the original value, then update its value.
    - Return the updated dictionary.
    """
    if not isinstance(dct, dict): #isintance compare if object dct is a dict. When false it will trigger next line
        raise ValueError("Input must be a dictionary") #exception handing on message of input value is not a dictionary. Example non-key value pair

    if key in dct: #check if key is found in dct
        print(f"Key '{key}' already exists with value: {dct[key]}") # print the duplicate key and set the object {dct[key]}

    dct[key] = value  # Update or add the key-value pair. Default Dict will update with latest data if we define DICT with new value.

    return dct # return to dict

# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26

# Test Case 1: Adding a new key to an empty dictionary
dict1 = {}
result1 = update_dictionary(dict1, "name", "Alice") #update dictionary with new key-Value name:Alice, Ordered all new data will be placed last
print(result1)  # Output: {'name': 'Alice'}

# Test Case 2: Updating an existing key in a dictionary
dict2 = {"age": 25} # define age is 25
result2 = update_dictionary(dict2, "age", 26) # Dict will update the latest value for key value pair and discard the old data.
# Output: Key 'age' already exists with value: 25
print(result2)  # Output: {'age': 26}
