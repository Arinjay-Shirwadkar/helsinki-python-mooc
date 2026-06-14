n=int(input("Please type in a number"))
while n>0:
    fact=1
    m=n
    while m>1:
        fact*=m
        m-=1
    print(f"The factorial of the number {n} is {fact}")
    n=int(input("Please type in a number:"))
print("Thanks and bye!")

