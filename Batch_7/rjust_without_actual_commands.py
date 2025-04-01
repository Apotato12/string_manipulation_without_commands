user_input = input("Please enter a string: ")
width = int(input("Please enter the total width: "))

spaces = width - len(user_input)

if spaces > 0:
        
        justified_string = ' ' * spaces + user_input

else:
        
        justified_string = user_input

print("Justified string:", justified_string)
