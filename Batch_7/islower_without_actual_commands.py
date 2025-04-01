# Program 4
# Atienza, Rein Gabriel
# BSPCE 1-2

def iflowercase():
    """Checks if all characters in the input string are lowercase without using the islower() function."""
    user_input = input("Please enter a sentence: ")

    for char in user_input:
        if ('a' <= char <= 'z'):

            print("all characthers are lowercase.")
            
        else:

            print("all characthers are not lowercase.")
            break

iflowercase()