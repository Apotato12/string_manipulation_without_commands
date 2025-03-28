sentence = input("Enter a sentence: ")

words = sentence.split()
    
title = []

for word in words:

    if len(word) > 0:
        title_cased = word[0].upper() + word[1:].lower()
        title.append(title_cased)

    else:
        title.append(word) 

result = ' '.join(title)

print("Result:", result)