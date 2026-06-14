def squared(s,n):
    i=0
    j=0
    c=0
    while i<n:
        while j<n:
            print(s[c], end="")
            c+=1
            if c>=len(s):
                c=0
            j+=1
        print()
        i+=1
        j=0

if __name__=="__main__":
    squared("Hey",5)