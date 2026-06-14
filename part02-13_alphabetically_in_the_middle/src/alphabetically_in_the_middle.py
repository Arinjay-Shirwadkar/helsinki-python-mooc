l1 = input("1st letter:")
l2 = input("2nd letter:")
l3 = input("3rd letter:")

if (l1>l2 and l2>l3) or (l2>l1 and l3>l2) :
    m=l2
elif (l2>l1 and l1>l3) or (l1>l2 and l3>l1):
    m=l1
else:
     m=l3
print("The letter in the middle is",m)