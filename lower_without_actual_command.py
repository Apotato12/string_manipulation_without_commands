input_string = input("Enter a string: ")

result = ""

for char in input_string:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char

print(result)