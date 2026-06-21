def who_won(mat: list):
    p1=0
    p2=0
    for arr in mat:
        for i in arr:
            if i==1:
                p1+=1
            elif i==2:
                p2+=1
            
    if p1>p2:
        return 1
    elif p2>p1:
        return 2
    else:
        return 0