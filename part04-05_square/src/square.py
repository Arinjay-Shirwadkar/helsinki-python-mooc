def line(n, s):
    if s!="":
        print(s[0]*n)
    else:
        print("*"*n)

def square(size, character):
    temp=size
    while temp>0:
     line(size, character)
     temp-=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")