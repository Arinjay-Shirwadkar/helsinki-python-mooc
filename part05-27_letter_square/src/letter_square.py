#Layers: 4

#DDDDDDD
#DCCCCCD
#DCBBBCD
#DCBABCD
#DCBBBCD
#DCCCCCD
#DDDDDDD

lay = int(input("Layers: "))
active = chr(ord('A')+lay-1) #active character, which provides filling
frills = ""
width=2*lay-1
rows = []
for r in range(1,lay+1):
    rows.append(frills+active*(width-2*len(frills))+frills[::-1])
    frills+=active
    print(rows[-1])
    active=chr(ord(active)-1)

for i in range(len(rows)-2,-1,-1):
    print(rows[i])
