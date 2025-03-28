input_string = input("Enter a string: ")
width = int(input("Enter the desired width: "))

fillchar = ' '
result = fillchar * max(0, width - len(input_string)) + input_string

print("Result:", result)
