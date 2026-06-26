while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    choice = input("Function: ")
    if choice=='1':
        f = input("The word in Finnish: ")
        e = input("The word in English: ")
        with open("dictionary.txt",'a') as file:
            file.write(f"{f};{e}\n")
        print("Dictionary entry added")
    elif choice=='2':
        s= input("Search term: ")
        with open("dictionary.txt") as file:
            for line in file:
                line = line.strip()
                words = line.split(";")
                if s in words[0] or s in words[1]:
                    print(f"{words[0]} - {words[1]}")
                
    else:
        print("Bye!")
        break