# Program 7
# Atienza, Rein Gabriel
# BSCPE 1-2
def center():
    """Adds space characters at the beginning and at the end of the string to center it within the specified width without using center() function."""
    input_string = input("Enter a string: ")
    width = int(input("Enter the desired width: "))

    total_spaces = max(0, width - len(input_string))

    left_padding = total_spaces // 2

    right_padding = total_spaces - left_padding

    result = ' ' * left_padding + input_string + ' ' * right_padding

    print("Result:", result)

center()