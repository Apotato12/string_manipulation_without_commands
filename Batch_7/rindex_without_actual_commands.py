# Program 10
# Atienza, Rein Gabriel
# BSPCE 1-2
def rindex():
    """Finds the last index of a specified word in the input string without using rindex()."""
    user_input = input("Please enter a string: ")
    word = input("Please enter the word to find: ")


    for i in range(len(user_input) - len(word), -1, -1):
            if user_input[i:i + len(word)] == word:
                print(f"The word '{word}' is found at index {i}.")

rindex()