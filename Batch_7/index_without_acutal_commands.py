user_input = input("Please enter a string: ")
word = input("Please enter the word to find: ")

index = -1

for i in range(len(user_input) - len(word) + 1):
        if user_input[i:i + len(word)] == word:

            print(f"The word '{word}' is found at index {i}.")
            break
        else:
              print("the word is not found")