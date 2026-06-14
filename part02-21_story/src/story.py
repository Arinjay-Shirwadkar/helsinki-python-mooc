words=""
c =0
s=""
while True:
    lastword = s
    s = input("Please type in a word:")
    if s==lastword:
        break
    if s!="end":
     if c==0:
         words = words+s
         
         c+=1
     else:
         words = words+" "+s

    else:
        break
print(words)