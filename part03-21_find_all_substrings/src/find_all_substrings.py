s = input()
c = input()
i =0
while i<len(s):
    if s[i]==c and i+2<len(s):
          print(s[i:i+3])
    i+=1
