def length_of_longest(lis):
    max = 0
    
    for s in lis:
        if len(s)>max:
            max=len(s)
            
    return max
    

