import random
def words(n: int, s: str):
    lis =[]
    with open('words.txt') as file:
        for line in file:
            if line.startswith(s):
                lis.append(line.strip())
    return random.sample(lis,n)