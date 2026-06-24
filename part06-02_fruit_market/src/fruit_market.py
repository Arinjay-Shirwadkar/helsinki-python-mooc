def read_fruits():
    dic={}
    with open("fruits.csv") as file:
        for line in file:
            line.replace("\n","")
            text = line.split(";")
            dic[text[0]]=float(text[1])
    return dic

