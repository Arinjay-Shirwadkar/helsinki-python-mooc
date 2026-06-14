def chessboard(n):
    i=0
    while i<n:
        j=0
        while j<n:
          if (i+2)%2==0:
            if (j+2)%2==0:
              print("1", end="")
            else:
              print("0", end="")
          else:
             if (j+2)%2==0:
              print("0", end="")
             else:
              print("1", end="")

          j+=1       
        print()
        i+=1

# Testing the function
if __name__ == "__main__":
    chessboard(3)