def remove_special_characters(s: str):
    st=""
    for char in s:
        if char.isalnum() or char.isspace():
            st+=char
    return st

def split_in_half(s: str):
    n = len(s)
    n=n//2
    return (s[:n],s[n:])

def change_case(s: str):
    st = ""
    for char in s:
        if char.islower():
            st+=char.upper()
        else:
            st+=char.lower()
    return st