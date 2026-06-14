n= int(input("How many students on the course?"))
size = int(input("Desired group size?"))

if (n%size)!=0:
    n+=size
print("Number of groups formed:",(n//size))