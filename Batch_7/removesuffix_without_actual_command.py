# Program 2
# Atienza, Rein Gabriel
# BSPCE 1-2

def removesuffix():
    """Removes the specified suffix from the end of the input string if it exists."""
    user_input = input("Please enter a string: ")
    
    suffix = input("Please enter the suffix to remove: ")

    if user_input.endswith(suffix):
        result = user_input[:-len(suffix)]
    else:
        result = user_input 

    print("Result:", result)

removesuffix()