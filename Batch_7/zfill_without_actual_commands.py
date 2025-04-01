user_input = input("Please enter a number: ")
zero = int(input("Please enter the total number of 0's: "))

zeros_needed = zero - len(user_input)

if zeros_needed > 0:

        zero_string = '0' * zeros_needed + user_input
else:

        zero_string = user_input

print("Zero-filled string:", zero_string)