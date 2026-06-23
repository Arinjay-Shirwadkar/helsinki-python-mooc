def oldest_person(people: list):
    min=float('inf')
    for person in people:
        if person[1]<min:
            min=person[1]
            oldest=person[0]
    return oldest