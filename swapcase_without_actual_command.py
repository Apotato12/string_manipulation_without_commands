# Program 8
# Atienza, Rein Gabriel
# BSCPE 1-2
def swapcase():
    """Reverses the casing of each character in the string without using swapcase() function."""
    input_string = input("Enter a string: ")
    
    result = ""
    
    for char in input_string:

        if 'a' <= char <= 'z': 
            result += char.upper() 

        elif 'A' <= char <= 'Z': 
            result += char.lower() 
        else:
            result += char 

    print("Result:", result)

swapcase()