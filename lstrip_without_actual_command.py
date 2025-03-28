# Program 1
# Atienza, Rein Gabriel
# Bscpe 1-2
def no_lstrip():
    """Allows the user to input a name and prints it without leading spaces."""
    input_name = input("Enter your name: ")

    index = 0

    while index < len(input_name) and input_name[index] == ' ':
        index += 1

    print(input_name[index:]) 

no_lstrip()