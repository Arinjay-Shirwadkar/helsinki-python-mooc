def shortest(lis):
    min = len(lis[0])
    mins=""
    for s in lis:
        if len(s)<min:
            min=len(s)
            mins=s
            
    return mins
    