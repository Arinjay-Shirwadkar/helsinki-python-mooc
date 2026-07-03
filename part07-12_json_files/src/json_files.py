import json

def print_persons(filename: str):
    with open(filename) as file:
        data = file.read()

    things = json.loads(data)
    for thing in things:
        print(f"{thing['name']} {thing['age']} years (",end='')
        for hobby in thing['hobbies']:
            if hobby != thing['hobbies'][0]:
                print(' ',end='')
            print(f"{hobby}",end='')
            if hobby!=thing['hobbies'][-1]:
                print(',',end='')
        print(")")

if __name__ == "__main__":
    print_persons('file1.json')
    
    