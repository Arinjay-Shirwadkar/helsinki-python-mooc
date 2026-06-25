def read_file(filename):
    new = 1 # used to indicate a new recipe
    recipes=[]
    temp=[]
    with open(filename) as file:
        for line in file:
            if line=='\n':
                recipes.append(temp)
                temp=[] #reassigning reference
            else:
                temp.append(line.strip())
    recipes.append(temp) #for the last recipe
    #print(recipes)
    return recipes

def search_by_name(filename: str, word: str):
    recipes = read_file(filename)
    lis = []
    for recipe in recipes:
        if word.lower() in (recipe[0]).lower():
            lis.append(recipe[0])
    
    return lis

def search_by_time(filename: str, prep_time: int):
    recipes = read_file(filename)
    lis = []
    for recipe in recipes:
        if int(recipe[1])<=prep_time:
            s=recipe[0]+", preparation time "+str(recipe[1])+" min"
            lis.append(s)
    return lis

def search_by_ingredient(filename: str, ingredient: str):
    recipes = read_file(filename)
    lis=[]
    for recipe in recipes:
        for element in recipe:
            if element==ingredient:
                s=recipe[0]+", preparation time "+str(recipe[1])+" min"
                lis.append(s)
    return lis


if __name__ == "__main__":
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")

    for recipe in found_recipes:
     print(recipe)
