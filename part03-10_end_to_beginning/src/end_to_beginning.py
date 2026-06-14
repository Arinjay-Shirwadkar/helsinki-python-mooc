s = input("Enter a string")

#i = len(s)-1
#while i>=0:
#    print(s[i])
#    i-=1

i=0
while i<len(s):
    print(s[-(1+i)])  #the maximum will be s[len(s)-(len(s))]
    i+=1