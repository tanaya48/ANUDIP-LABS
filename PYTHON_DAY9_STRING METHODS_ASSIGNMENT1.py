
#Write a Python program to Count all letters, digits, and special symbols from the given string
def count_characters(input_string):
    # Initialize counters for characters, digits, and symbols
    chars = 0
    digits = 0
    symbols = 0
    
    # Loop through each character in the input string
    for ch in input_string:
        # Check if the character is a letter (alphabet)
        if ch.isalpha():
            chars += 1  # Increment character counter
        # Check if the character is a digit
        elif ch.isdigit():
            digits += 1  # Increment digit counter
        # If it's neither a letter nor a digit, it's a special symbol
        else:
            symbols += 1  # Increment symbol counter
            
    # Return the counts as a tuple
    return chars, digits, symbols

# Input string to test the function
input_string = "P@#yn26at^&i5ve"

# Call the function and store the result
chars, digits, symbols = count_characters(input_string)

# Print the results
print(f"Chars = {chars}")
print(f"Digits = {digits}")
print(f"Symbols = {symbols}")

"""
OUTPUT
Chars = 8
Digits = 3
Symbols = 4

"""

