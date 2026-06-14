s = input()
sub = input()
c=0
i=len(sub)-1 #no need to start at 0
pos =-1
p1=0
updated =0

while i<len(s):
    wind = s[p1:i+1]
    if wind==sub:
        if c==1:
            pos = i+1-len(sub)
            break
        c+=1
        updated = 1

    if updated==1: #jump the whole length of the substring so overlap will be avoided
        p1+=len(sub)
        i+=len(sub)
        updated =0
    else:
     p1+=1
     i+=1

if pos!=-1:
    print(f"The second occurrence of the substring is at index {pos}.")
else:
    print("The substring does not occur twice in the string.")

    
