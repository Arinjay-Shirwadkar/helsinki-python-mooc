n = int(input())
i=1
while i<=n:
    if i+1>n:
        print(i)
        break
    else:
        print((i+1),"\n",(i),sep="")
        i+=2
        