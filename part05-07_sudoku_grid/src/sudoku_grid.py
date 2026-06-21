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
    
def sudoku_grid_correct(mat):
    for i in range(0,9):
        if not (row_correct(mat,i) and column_correct(mat,i)):
            return False
    for i in range(0,7,3):
        for j in range(0,7,3):
            if not block_correct(mat,i,j):
                return False
    return True