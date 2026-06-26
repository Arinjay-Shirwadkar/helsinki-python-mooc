while(True):
        print("1 - add an entry, 2 - read entries, 0 - quit")
        ch = input('Function: ')
        if ch=='0':
            print("Bye now!")
            break
        elif ch=='1':
            e = input("Diary entry: ")
            with open("diary.txt",'a') as file:
                file.write(e+'\n')
            print("Diary saved\n")
        else:
            print('Entries:')
            with open("diary.txt") as file:
                for line in file:
                    print(line)


            

