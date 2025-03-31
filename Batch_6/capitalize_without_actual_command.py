# Program 9
# Atienza, Rein Gabriel
# BSPCE 1-2
def capitalize():
    """Capitalizes the first letter of the string and makes all other letters lowercase without using capitalize() function."""
    sentence = input("Enter a sentence: ")

    if len(sentence) == 0:
        result = sentence
    else:
        result = sentence[0].upper() + sentence[1:].lower()

    print("Result:", result)

capitalize()