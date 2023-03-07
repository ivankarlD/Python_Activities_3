list = []
while True :
    word = input("Enter the word: ")
    list.append(word)
    again = input("Do you want to try again? Y/N: ")
    if again == "y" or again == "Y" : continue
    print(f"Total Number of Words: {len(list)}")
    for item in list : print(item)
    break
