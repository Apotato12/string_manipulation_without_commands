user_input = input("Please enter a string: ")
word = input("Please enter the word to count: ")

count = 0


for i in range(len(user_input) - len(word) + 1):
        if user_input[i:i + len(word)] == word:
            count += 1


print("the word appears " + str(count) + " times")