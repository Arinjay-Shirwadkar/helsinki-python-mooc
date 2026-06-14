lim = int(input('Limit:'))
runSum = 0
c=0
op = ""
while runSum<lim:
    c+=1
    if runSum+c<lim:
        op+= f"{c} + "
    else:
        op+=f"{c}"       


    runSum+=c
print(f"The consecutive sum: {op} = {runSum}")