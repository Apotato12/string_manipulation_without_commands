user_input = input("Please enter a sentence: ")

for char in user_input:
        if ('a' <= char <= 'z'):
            print("all characthers are lowercase.")
            
        else:
            print("all characthers are not lowercase.")
            break