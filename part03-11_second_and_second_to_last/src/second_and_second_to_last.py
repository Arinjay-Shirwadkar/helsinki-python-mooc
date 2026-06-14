s = input("Please type in a string")
if len(s)>1:
 if s[1]==s[-2]:
     print("The second and the second to last characters are "+s[1])
 else:
     print("The second and the second to last characters are different")
else:
    print("The second and the second to last characters are different")