# Program 3
# Atienza, Rein Gabriel
# BSPCE 1-2

def uppercase():
    """Converts all characters of the input string to uppercase without using the upper() function."""
    user_input = input("Please enter a sentence: ")
    
    capitalize = ""

    for char in user_input:
        if 'a' <= char <= 'z':

            capitalize += chr(ord(char) - 32)

        else:

            capitalize += char

    print("Result: " + capitalize)

uppercase()