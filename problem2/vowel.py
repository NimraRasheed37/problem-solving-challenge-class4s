# count vowels in string

def count_vowels(input_string):
    # Define the set of vowels (both lowercase and uppercase)
    vowels = set("aeiouAEIOU")
    # Initialize a counter for vowels
    count = 0
    # Loop through each character in the string
    for char in input_string:
        if char in vowels:
            count += 1
    return count

# prompt user for input
input_str = input("Enter a string: ")
output = count_vowels(input_str)
print(output)