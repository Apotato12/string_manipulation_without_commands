# Program 4
# Atienza, Rein Gabriel
# BSCPE 1-2
def check_all():
    """Checks if all characters of the string are uppercase without using the isupper() function."""
    input_string = input("Enter a string: ")

    all_upper = True

    for char in input_string:
        if not ('A' <= char <= 'Z'):
            all_upper = False
            break

    if all_upper:
        print("All characters are uppercase.")
    else:
        print("Not all characters are uppercase.")

check_all()