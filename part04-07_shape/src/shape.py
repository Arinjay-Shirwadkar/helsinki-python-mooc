def line(n, s):
    if s!="":
        print(s[0]*n)
    else:
        print("*"*n)

def shape(t,c1,r,c2):
    i=1
    while i<=t:
        line(i,c1)
        i+=1
    i=1
    while i<=r:
        line(t,c2)
        i+=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")