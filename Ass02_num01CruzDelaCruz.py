# dictionary
dict = {}
choice = ""

while True :
    print("Record Keeping App\na. Add Data\nb. Delete Data\nc. End")
    choice = input("Enter your choice: ")
    if choice == "a" : 
        print("=======ADD NEW RECORD==========")
        key = input("Enter Key: ")
        # value = input("Enter Value: ")
        dict[key] = input("Enter Value: ")
    elif choice == "b" :
        dict.pop(input("Enter Key: "))
    elif choice == "c" :
        print("Thank you!")
        break
    else : 
        break

    print("=======DISPLAY RECORD==========")
    for key in dict :
        print(f"{key} : {dict[key]}")
    print("=======END OF RECORD==========")


