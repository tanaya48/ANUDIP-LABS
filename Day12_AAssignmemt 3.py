# Define a function to find duplicate values in a list
def find_duplicates(lst):
    # Create an empty list to store duplicates
    duplicates = []
    
    # Loop through each item in the list
    for i in range(len(lst)):
        # Compare the current item with every other item in the list
        for j in range(i + 1, len(lst)):
            # If the two items are the same and the item is not already in the duplicates list
            if lst[i] == lst[j] and lst[i] not in duplicates:
                # Add the item to the duplicates list
                duplicates.append(lst[i])
    
    # Return the list of duplicates
    return duplicates

# Example list to test the function
example_list = [1, 5, 2, 1, 3, 5, 7, 8, 9, 3, 2]

# Call the function and store the duplicates
duplicates = find_duplicates(example_list)

# Print the duplicates if found, otherwise display a message
if duplicates:
    print("Duplicate values in the list are:", duplicates)
else:
    print("No duplicate values found.")
"""
OUTPUT
Duplicate values in the list are: [1, 5, 2, 3]
"""
