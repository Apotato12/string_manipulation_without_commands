# Program 8
# Atienza, Rein Gabriel
# BSCPE 1-2
def ends_with():
    """Checks if the string ends with the specified suffix without using the endswith() function."""
    input_sentence = input("Enter a string: ")
    suffix = input("Enter the suffix to check: ")

    suffix_length = len(suffix)

    if len(input_sentence) >= suffix_length:
        if input_sentence[-suffix_length:] == suffix:
            print("The string ends with the specified suffix.")
        else:
            print("The string does not end with the specified suffix.")

ends_with()