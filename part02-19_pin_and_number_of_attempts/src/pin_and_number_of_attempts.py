c=0

while True:
    p = int(input("PIN:"))
    c+=1
    if(p==4321):
        if(c==1):
            print("Correct! It only took you one single attempt!")
            break
        else : 
            print(f"Correct! It took you {c} attempts")
            break

    else:
        print("Wrong")
