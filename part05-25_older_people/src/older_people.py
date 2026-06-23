def older_people(people: list, year: int):
    sol=[]
    for person in people:
        if person[1]<year:
            sol.append(person[0])
    return sol