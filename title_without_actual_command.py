# Program 10
def custom_title():
    """Capitalizes the first letter of each word in the string and makes all other letters lowercase without using title() function."""
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

custom_title()