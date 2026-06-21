def column_correct(mat: list, c: int):
    hash = []
    for i in range(0,10):
        hash.append(0)

    for r in mat:
        i=r[c]
        if i!=0 and (hash[i]!=0 or i<0 or i>9):
            return False
        else:
            hash[i]+=1
    return True
    
