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