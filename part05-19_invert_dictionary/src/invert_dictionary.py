def invert(dic: dict):
    dicopy={}
    for k in dic:
        dicopy[dic[k]]=k
    dic.clear()
    dic.update(dicopy)