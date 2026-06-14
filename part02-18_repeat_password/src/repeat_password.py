pass1 = input("Enter password:")

while True:
    pass2 = input("Repeat password:")
    if pass2==pass1:
        break
    else:
        print("They do not match!")
print("User account created!")