# Program 3
# Atienza, Rein Gabriel
# BSCPE 1-2
def capital_to_lowercase():
    """Converts all characters of the string into lowercase without using the lower() function."""
    input_string = input("Enter a string: ")
    
    result = ""
    
    for char in input_string:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char

    print("String in lowercase:", result)

capital_to_lowercase()