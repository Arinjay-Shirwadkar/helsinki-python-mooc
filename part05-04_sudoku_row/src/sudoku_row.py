def row_correct(mat: list, r: int):
    hash = []
    for i in range(0,10):
        hash.append(0)
    for i in mat[r]:
        if i!=0 and (hash[i]!=0 or i<0 or i>9):
            return False
        else:
            hash[i]+=1
    return True
    
