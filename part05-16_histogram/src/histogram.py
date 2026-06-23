def histogram(s):
    dict = {}
    for c in s:
        if c not in dict:
            dict[c]=0
        dict[c]+=1
    for i in dict:
        print(i," ","*"*dict[i],sep="")