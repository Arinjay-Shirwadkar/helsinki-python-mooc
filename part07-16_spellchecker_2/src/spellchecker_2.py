from difflib import get_close_matches

s = input("Write text: ")
words = {} # I have to use a dictionary in order to minimize the time for lookups
wordss = []

with open("wordlist.txt") as file:
    for line in file:
        words[(line.strip()).lower()]=1
        wordss.append((line.strip()).lower())

givenwords = s.split(" ")

wrong_words = []

for word in givenwords:
    if word.lower() not in words:
        wrong_words.append(word)
        word='*'+word+'*'      
    print(word,end=" ")

if len(wrong_words)!=0:
    print('\nsuggestions:')

for wrong_word in wrong_words:
    print(f"{wrong_word}: ",end="")
    damn = get_close_matches(wrong_word,wordss)
    for ahh in damn:
        
        print(f"{ahh}",end="")
        if ahh!= damn[-1]:
            print(", ",end="")
    print()

