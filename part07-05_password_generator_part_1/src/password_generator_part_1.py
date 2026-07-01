from random import randint

def generate_password(n):
    s=""
    for i in range(0,n):
        j = randint(0,25)
        s+= chr(j+ord('a'))
    return s

if __name__ == "__main__":
    for i in range(10):
        print(generate_password(8))