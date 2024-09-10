#Write a Python program to get the largest and smallest number from a list without builtin functions. 
# Define a function to find the largest and smallest numbers in a list
def find_largest_smallest(lst):
    # Assume the first element is both the largest and smallest
    largest = lst[0]
    smallest = lst[0]
    
    # Loop through each element in the list starting from the second element
    for item in lst[1:]:
        # If the current item is greater than the largest, update the largest
        if item > largest:
            largest = item
        
        # If the current item is smaller than the smallest, update the smallest
        if item < smallest:
            smallest = item
    
    # Return both the largest and smallest numbers
    return largest, smallest

# Example list to test the function
example_list = [23, 1, 45, -10, 99, 34, -2, 0]

# Call the function and store the results
largest, smallest = find_largest_smallest(example_list)

# Print the results
print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)

"""
OUTPUT
The largest number in the list is: 99
The smallest number in the list is: -10
"""
