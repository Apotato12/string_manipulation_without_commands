user_input = input("Please enter a string: ")
word = input("Please enter the substring to find: ")


for i in range(len(user_input) - len(word), -1, -1):
        if user_input[i:i + len(word)] == word:
            print(f"The word '{word}' is found at index {i}.")