def largest():
    num=0
    with open("numbers.txt") as new_file:
        
        for line in new_file:
            s=line.replace("\n","")
            n=int(s)
            if n>num:
                num=n
    return num


