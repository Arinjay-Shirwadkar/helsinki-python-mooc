f1 = input("Student information: ") #students1.csv
f2 = input("Exercises completed: ")#exercises1.csv

#f1 = "students1.csv"
#f2 = "exercises1.csv"

dic1={}
with open(f1) as file1:
    skip=1
    for line in file1:
        if skip==1:
            skip=0
            continue
        
        s = line.split(";")

        dic1[s[0]]= s[1]+" "+s[2].strip()

dic2={}
skip=1

with open(f2) as file2:
    skip=1
    for line in file2:
        if skip==1:
            skip=0
            continue
        
        lis = line.split(";")
        Sum=0
        lis[-1]=lis[-1].strip()
        for num in range(1,len(lis)):
            Sum+=int(lis[num])
        dic2[lis[0]]= Sum

for id,name in dic1.items():
    print(name,dic2[id])
