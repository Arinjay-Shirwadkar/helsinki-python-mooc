dic={}
while True:
    ch = input("command (1 search, 2 add, 3 quit): ")
    if ch=='3':
        break
    elif ch=='1':
        s =input("name: ")
        if s in dic:
            for i in dic[s]:
                print(i)
        else:
            print("no number")
    elif ch=='2':
        s =input("name: ")
        if s not in dic:
            dic[s]=[]
        n =input("number: ")
        print("ok!")
        (dic[s]).append(n)
    

print("quitting...")
