def most_common_character(s):
    hash =[]
    max=0
    
    for c in s:
        if s.count(c)>max:
            max=s.count(c)
            maxS=c
    return maxS

        

