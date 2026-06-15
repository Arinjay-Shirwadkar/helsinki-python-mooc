def line(n, s):
    if s!="":
        print(s[0]*n)
    else:
        print("*"*n)

def square_of_hashes(size):
   temp=size
   while temp>0:
     line(size, "#")
     temp-=1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
