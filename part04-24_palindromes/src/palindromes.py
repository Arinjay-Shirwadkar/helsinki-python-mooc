def palindromes(s):
    p1=0
    p2=len(s)-1
    while True:
        if p1>=p2:       
            return True 

        if s[p1]!=s[p2]: 
            return False
        else:
            p1=p1+1
            p2=p2-1

while True:      
    s = input("Please type in a palindrome: ")
    if palindromes(s):
        print(s,"is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")

