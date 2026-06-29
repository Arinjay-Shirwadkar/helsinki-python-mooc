import string
def separate_characters(s:str) -> tuple:
    letters = string.ascii_letters
    punc = string.punctuation
    space = string.whitespace
    l = ""
    p = ""
    sp = ""
    
    for char in s:
        if char in letters:
            l+=char
        elif char in punc:
            p+=char
        else:
            sp+=char
        
    return(l,p,sp)
