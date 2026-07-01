# Die A has the sides 3, 3, 3, 3, 3, 6
#Die B has the sides 2, 2, 2, 5, 5, 5
#Die C has the sides 1, 4, 4, 4, 4, 4
import random
def roll(s):
    if s=='A':
        return random.choice([3,3,3,3,3,6])
    elif s=='B':
        return random.choice([2, 2, 2, 5, 5, 5])
    elif s=='C':
        return random.choice([1, 4, 4, 4, 4, 4])
    
def play(die1: str, die2: str, times: int):
    un=0
    dos=0
    tres=0
    for i in range(0,times):
        r1 = roll(die1)
        r2 = roll(die2)
        if r1>r2:
            un+=1
        elif r1<r2:
            dos+=1
        else:
            tres+=1
    return (un,dos,tres)
