input_name = input("enter your name: ")

index = 0

while index < len(input_name) and input_name[index] == ' ':
        index += 1

print (input_name[index:]) 