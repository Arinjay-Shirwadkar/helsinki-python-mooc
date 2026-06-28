def read_input(s,l,u):
    while True:
        try:
            n = int(input(s))
            if n>=l and n<=u:
                return n
        except ValueError:
            pass
        
        print(f"You must type in an integer between {l} and {u}")

#number = read_input("Please type in a number: ", 5, 10)
#print("You typed in:", number)

