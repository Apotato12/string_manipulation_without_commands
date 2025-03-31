def prefix():
    """Removes the specified prefix from the beginning of the string if it exists."""
    input_string = input("Enter a string: ")
    prefix = input("Enter the prefix to remove: ")

    if input_string.startswith(prefix):
        result = input_string[len(prefix):]
    else:
        result = input_string

    print("Result:", result)

prefix()