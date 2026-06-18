def distinct_numbers(lis):
    liss = sorted(lis)
    lisd=[]
    for i in range(len(liss)):
        if i>0:    
            if liss[i-1]==liss[i]:
                continue
            else:
                lisd.append(liss[i])
        else:
            lisd.append(liss[i])
        
    return lisd
