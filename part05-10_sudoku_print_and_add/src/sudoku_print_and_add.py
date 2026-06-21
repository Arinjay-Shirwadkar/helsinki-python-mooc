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

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
   sudoku[row_no][column_no]=number

if __name__=="__main__":
    sudoku  = [[1, 0, 0, 0, 0, 0, 0, 0, 0],[2, 0, 0, 0, 0, 0, 0, 0, 0],[3, 0, 0, 0, 0, 0, 0, 0, 0],[4, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print_sudoku(sudoku)