user_input = input("Please enter a string: ")

index = len(user_input) - 1

while index >= 0:
    if user_input[index] != ' ' :
        break
    index -= 1

result = user_input[:index + 1]

print("result: " + result)