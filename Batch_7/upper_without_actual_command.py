user_input = input("Please enter a sentence: ")
capitalize = ""

for char in user_input:
        
    if 'a' <= char <= 'z':
        capitalize += chr(ord(char) - 32)

    else:
        capitalize += char

print("Result:" + capitalize)