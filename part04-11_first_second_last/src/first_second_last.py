def first_word(s):
    p=0
    while(True):
        if s[p+1]==' ':
            break #2 words are guaranteed so no further checks are required
        p+=1
    return s[:p+1]

def second_word(s):
    p1=0
    p2=0
    p=0
    c=0
    while(True):
        if s[p-1]==' ':
            p1=p
        if p==len(s)-1 or s[p+1]==' ':
            c+=1
            if c==2:
                p2=p
                break

            
        p+=1
    return s[p1:p2+1]
    
def last_word(s):
    i=len(s)-1
    while(True):
        if s[i]==' ':
            return s[i+1:]
        i-=1
        
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))