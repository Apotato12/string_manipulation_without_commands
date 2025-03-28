input_string = input("Enter a string: ")
prefix = input("Enter the prefix to remove: ")

if input_string.startswith(prefix):
    result = input_string[len(prefix):]
else:
    result = input_string

print("Result:", result)