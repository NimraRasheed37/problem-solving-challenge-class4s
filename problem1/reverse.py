# reverse any string entered by user using slicing method in python
def reverse_string(input_string):
    return input_string[::-1] # it is a slicing operation that reverses the string.

# prompt user for input
input_str = input("Enter a string: ")
output_str = reverse_string(input_str)
print(output_str)