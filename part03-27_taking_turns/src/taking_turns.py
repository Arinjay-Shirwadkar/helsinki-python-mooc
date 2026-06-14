n = int(input())
fromStart = 0
fromEnd=0
c=0

while c!=n:
    if (c+2)%2==0:
        print(1+fromStart)
        fromStart+=1
    else:
        print(n-fromEnd)
        fromEnd+=1
    c+=1
