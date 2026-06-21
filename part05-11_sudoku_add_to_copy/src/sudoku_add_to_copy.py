def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    copy = sudoku[:]
    for i in range(0,9):
        copy[i]=sudoku[i][:]        

    copy[row_no][column_no]=number
    print_sudoku(copy)
    return copy

def print_sudoku(mat):
    for i in range(0,9):
        if i%3==0:
           print()
        for j in range(0,9):
            if j==8:
             if mat[i][j]!=0:
                 print (mat[i][j],end='')
             else:
                print("_",end='')                
             continue
             
            if j!=0 and j%3==0:
                print(' ',end="")
            if mat[i][j]!=0:
                print (mat[i][j],end=' ')
            else:
               print("_",end=' ')
        print()

if __name__=="__main__":
    sudoku  = [[1, 0, 0, 0, 0, 0, 0, 0, 0],[2, 0, 0, 0, 0, 0, 0, 0, 0],[3, 0, 0, 0, 0, 0, 0, 0, 0],[4, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]]
    copy_and_add(sudoku,5,5,5)
    copy_and_add(sudoku,6,5,5)
    copy_and_add(sudoku,7,5,5)
    copy_and_add(sudoku,8,5,5)
