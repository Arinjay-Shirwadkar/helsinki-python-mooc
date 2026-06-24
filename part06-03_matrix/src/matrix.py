def read_matrix():
    mat=[]
    with open("matrix.txt") as file:
        for line in file:
            line.replace("\n","")
            row = line.split(",")
            introw=[]
            for s in row:
                introw.append(int(s))
            mat.append(introw)
    return mat

def matrix_sum():
    mat=read_matrix()
    Sum=0
    for row in mat:
        for num in row:
            Sum+=num
    return Sum

def matrix_max():
    mat=read_matrix()
    max=float('-inf')
    for row in mat:
        for num in row:
            if num>max:
                max=num
    return max

def row_sums():
    mat=read_matrix()
    sums=[]
    for row in mat:
        sums.append(sum(row))
    return sums



