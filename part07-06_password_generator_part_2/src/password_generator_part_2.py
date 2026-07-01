import random
import string

def generate_strong_password(n, c1, c2):
    c =c1
    c1=c2
    c2=c
    s=""
    letters = string.ascii_lowercase
    randos = '!?=+-()#'
    nums = string.digits
    #we pick the first three from each and then the rest doesn't matter
    cons =1
    s+= random.sample(letters,1)[0]
    remaining = letters
    if c1:
        cons+=1
        s+=random.sample(randos,1)[0]
        remaining+= randos
    if c2:
        cons+=1
        s+=random.sample(nums,1)[0]
        remaining+=nums
    
    for i in range(1,n+1-cons):
        j = random.sample(remaining,1)[0]
        s+= j
    return ("".join(random.sample(s,len(s))))

if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(5,True,False))