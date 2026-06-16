def greatest_number(a,b,c):
    if c>=a and c>=b:
        return c
    elif b>=a and b>=c:
        return b
    elif a>=b and a>=c:
        return a
# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(155, 4, 8)
    print(greatest)