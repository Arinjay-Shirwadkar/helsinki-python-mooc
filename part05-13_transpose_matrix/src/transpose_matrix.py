def transpose(mat: list):

    for i in range(0,len(mat)):
        for j in range(0,len(mat[i])):
            if j>=i:
                c=mat[i][j]
                mat[i][j]=mat[j][i]
                mat[j][i]=c