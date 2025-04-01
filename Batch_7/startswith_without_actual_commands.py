# Program 5
# Atienza, Rein Gabriel
# BSPCE 1-2

def starts_with():
    """Checks if the input string starts with the specified prefix without using the startswith() function."""
    sentence = input("Please enter a string: ")

    word = input("Please enter the word to check: ")

    for i in range(len(word)):
            
            if sentence[i] != word[i]:
                print("The string does not start with the specified prefix.")

            else:
                print("The string starts with the specified prefix.")

starts_with()