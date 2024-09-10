#Write a Python program to sum all the items in a list
# Define a function to sum all the items in a list
def sum_of_list(lst):
    # Initialize a variable to store the sum of the items
    total_sum = 0
    
    # Loop through each item in the list
    for item in lst:
        # Add each item to the total sum
        total_sum += item
    
    # Return the total sum of the items
    return total_sum

# Example list to test the function
example_list = [1, 2, 3, 4, 5]

# Call the function and print the result
result = sum_of_list(example_list)
print("The sum of the items in the list is:", result)

"""
Output
The sum of the items in the list is: 15
"""
