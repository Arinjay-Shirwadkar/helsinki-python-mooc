lis =[]
while True:
    s = input("Word: ")
    if s in lis:
        print  ("You typed in",len(lis),"different words")
        break
    else:
        lis.append(s)

