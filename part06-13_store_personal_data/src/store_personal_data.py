def store_personal_data(person: tuple):
    with open("people.csv",'a') as file:
        file.write(person[0]+';'+str(person[1])+';'+str(person[2])+'\n')