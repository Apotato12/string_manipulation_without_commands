# Program 6
# Atienza, Rein Gabriel
# BSPCE 1-2

def r_justify():
    """Adds space characters at the beginning of the string to reach the specified length without using rjust()."""
    user_input = input("Please enter a string: ")
    
    width = int(input("Please enter the total width: "))

    spaces = width - len(user_input)

    if spaces > 0:
            
            justified_string = ' ' * spaces + user_input

    else:
            
            justified_string = user_input

    print("Justified string:", justified_string)

r_justify()
