# function to print sum of digits
def sum_of_digits(number):
    # Convert the number to a string to iterate over each digit
    return sum(int(digit) for digit in str(number))

# prompt user for input
input_num = input("Enter few digits: ")
output = sum_of_digits(input_num)
print(output)  