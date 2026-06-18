def all_the_longest(lis):
    max = 0
    maxLis =[]

    for s in lis:
        if len(s)>max:
            max=len(s)
            maxLis=[]
            maxLis.append(s)

        elif len(s)==max:
            maxLis.append(s)
    return maxLis            