name = input("Whom should I sign this to: ") #Ada
file =  input("Where shall I save it: ") #inscribed.txt

with open(file, 'w') as mine:
    mine.write(f"Hi {name}, we hope you enjoy learning Python with us! Best, Mooc.fi Team")