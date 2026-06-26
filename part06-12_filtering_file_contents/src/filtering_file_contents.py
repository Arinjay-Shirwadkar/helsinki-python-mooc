def filter_solutions():
    with open("correct.csv",'w') as fillet:
        pass
    with open("incorrect.csv",'w') as fillet:
        pass
    with open("solutions.csv") as file:
        for line in file:
            things = (line.strip()).split(";")
            #ops = things[1].split("+")
            ops=[]
            for i in range(1,len(things[1])):
                if things[1][i]=='+':
                    ops.append(things[1][:i])
                    ops.append(things[1][i+1:])

                    if int(ops[0]) + int(ops[1])==int(things[2]):
                        with open("correct.csv",'a') as anotherfile:
                            anotherfile.write(line)
                    else:
                        with open("incorrect.csv",'a') as yetanotherfile:
                            yetanotherfile.write(line)

                elif things[1][i]=='-':
                    ops.append(things[1][:i])
                    ops.append(things[1][i+1:])

                    if int(ops[0]) - int(ops[1])==int(things[2]):
                        with open("correct.csv",'a') as anotherfile:
                            anotherfile.write(line)
                    else:
                        with open("incorrect.csv",'a') as yetanotherfile:
                            yetanotherfile.write(line)
    