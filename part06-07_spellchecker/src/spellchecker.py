s = input("Write text: ")
words = {} # I have to use a dictionary in order to minimize the time for lookups

with open("wordlist.txt") as file:
    for line in file:
        words[(line.strip()).lower()]=1

givenwords = s.split(" ")

for word in givenwords:
    if word.lower() not in words:
        word='*'+word+'*'
    print(word,end=" ")

    
