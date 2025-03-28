sentence = input("Enter a sentence: ")

if len(sentence) == 0:
        result = sentence 
else:
        result = sentence[0].upper() + sentence[1:].lower()

print("Result:", result)
