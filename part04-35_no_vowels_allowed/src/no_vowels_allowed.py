def no_vowels(s:str):
    st=""
    for c in s:
        if c=="a" or c=="e" or c=="i" or c=="o" or c=="u":
            continue
        else:
            st+=c
    return st
