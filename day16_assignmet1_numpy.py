# Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.
#  Input: my_list = [1, 2, 3, 4, 5]

# importing numpy library
import numpy as np

# Input list
my_list = [1, 2, 3, 4, 5]

# Convert list to numpy array
np_array = np.array(my_list)

# Display the numpy array
print("Numpy Array:", np_array)

# Display first and last element
print("First Element:", np_array[0])
print("Last Element:", np_array[-1])

# Multiply each element by 2 and display result
multiplied_array = np_array * 2
print("Multiplied Array:", multiplied_array)

# ans
# Numpy Array: [1 2 3 4 5]
# First Element: 1
# Last Element: 5
# Multiplied Array: [ 2  4  6  8 10]
