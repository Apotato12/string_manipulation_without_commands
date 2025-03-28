input_string = input("Enter a string: ")
width = int(input("Enter the desired width: "))

result = input_string + ' ' * max(0, width - len(input_string))

print("Result:", result)