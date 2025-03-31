# Program 1
# Atienza, Rein Gabriel
# BSPCE 1-2

def r_strip():
    """removes the end spaces from the end of the input string and returns the modified string."""
    user_input = input("Please enter a string: ")

    index = len(user_input) - 1

    while index >= 0:
        if user_input[index] != ' ':
            break
        index -= 1

    result = user_input[:index + 1]

    print("Result:", result)

r_strip()