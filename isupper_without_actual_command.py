input_string = input("Enter a string: ")

all_upper = True

for char in input_string:
    if not ('A' <= char <= 'Z'):
        all_upper = False

    if all_upper:
        print("this characters are uppercase.")
    else:
        print("Not all characters are uppercase.")