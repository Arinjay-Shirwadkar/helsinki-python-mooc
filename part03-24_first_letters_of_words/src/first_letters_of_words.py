s = input()
flag = 0 #0 means through space
i =0

while i<len(s):
    if flag==0 and s[i]!=' ':
        print(s[i])
        flag=1
    elif s[i]==' ':
        flag=0
    i+=1
    
