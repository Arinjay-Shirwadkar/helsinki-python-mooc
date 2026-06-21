def block_correct(mat: list, r: int,c):
    
    hash = []
    for i in range(0,10):
        hash.append(0)

    for i in range(r,r+3):
        for j in range(c,c+3):            
        
         if mat[i][j]!=0 and (hash[mat[i][j]]!=0 or mat[i][j]<0 or mat[i][j]>9):
            return False
         else:
            hash[mat[i][j]]+=1
    return True
    