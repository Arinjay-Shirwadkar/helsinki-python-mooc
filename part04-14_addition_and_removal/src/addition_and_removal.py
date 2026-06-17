arr = []
#The list is now []
#a(d)d, (r)emove or e(x)it: d
#The list is now [1]
i=1
while True:
 print("The list is now",arr)
 s = input("a(d)d, (r)emove or e(x)it: ")
 if s=='x':
  break
 elif s=="d":
  arr.append(i)
  i+=1
 elif s=='r':
  arr.pop(len(arr)-1)
  i-=1
 else:
  print("Please enter either d,r or x")
 
print("Bye!")
