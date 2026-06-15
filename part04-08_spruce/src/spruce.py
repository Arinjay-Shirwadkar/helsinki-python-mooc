def spruce(r):
    i=1
    print("a spruce!")
    while i<=r:
        print(" "*(r-i),end="")
        print("*"*(2*i-1))
        i+=1
    print(" "*(r-1),end="")
    print("*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(2)