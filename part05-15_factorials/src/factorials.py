def factorials(n: int):
    runProd=1
    i =1
    dict ={}
    while i<=n:
        runProd*=i
        dict[i]=runProd
        i+=1
    return dict
