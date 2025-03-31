user_input = input("Please enter a string: ")
suffix = input("Please enter the suffix to remove: ")

if user_input.endswith(suffix):
    result = user_input[:-len(suffix)]
else:
    result = user_input

print("Result:" + result)