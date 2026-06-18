def no_shouting(lis):
    finalist=[]
    for s in lis:
        if s.isupper():
            continue
        else:
            finalist.append(s)
    return finalist