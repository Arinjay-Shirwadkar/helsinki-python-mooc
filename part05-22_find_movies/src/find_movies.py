def find_movies(database: list, search_term: str):
    sol=[]
    for d in database:
        if search_term.lower() in d['name'].lower():
            sol.append(d)
    return sol