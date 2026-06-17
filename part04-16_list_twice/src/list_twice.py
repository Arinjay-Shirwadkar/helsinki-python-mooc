lis =[]

while True:
    n=int(input("New item: "))
    if n==0:
        break
    lis.append(n)
    print("The list now:",lis)
    print("The list in order:",sorted(lis))
print("Bye!")