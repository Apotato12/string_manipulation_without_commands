# Program 6
# Atienza, Rein Gabriel
# BSCPE 1-2
def ljust():
    """Adds space characters at the end of the string to reach the specified width without using ljust() function."""
    input_string = input("Enter a string: ")
    width = int(input("Enter the desired width: "))

    result = input_string + ' ' * max(0, width - len(input_string))

    print("Result:", result)

ljust()