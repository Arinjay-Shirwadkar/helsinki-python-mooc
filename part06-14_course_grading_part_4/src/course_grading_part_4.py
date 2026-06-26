f1 = input("Student information: ") #students1.csv
f2 = input("Exercises completed: ")#exercises1.csv
f3 = input("Exam points: ")
f4 = input("Course information: ")
#f1 = "students1.csv"
#f2 = "exercises1.csv"
#f3 = "exam_points1.csv"
#f4 = "course1.txt"
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
dic5={}
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
        dic5[lis[0]]=Sum
        
        perc=100*(Sum)/40
        points=perc//10
        #print(lis,perc,points)
        dic2[lis[0]]= points

skip=1
dic3={}
with open(f3) as file3:
    for line in file3:
        if skip==1:
            skip=0
            continue
        s=line.split(";")
        s[-1]=s[-1].strip()
        ints =[]
        for i in range(1,len(s)):
            ints.append(int(s[i]))
        dic3[s[0]]=sum(ints)
        #print(dic3[s[0]])

dic4={}
dic6={}
for studid, marks in dic3.items():
    currSum=dic2[studid]+marks
    dic6[studid]=currSum
    if currSum<=14:
        dic4[studid]=0
    elif currSum<=17:
        dic4[studid]=1
    elif currSum<=20:
        dic4[studid]=2
    elif currSum<=23:
        dic4[studid]=3
    elif currSum<=27:
        dic4[studid]=4
    elif currSum>=28:
        dic4[studid]=5

with open("results.txt",'w') as file:
    with open(f4) as ughh:
        for line in ughh:
            if "name:" in line:
                line = line.strip()
                course = line[6:]
            else:
                line = line.strip()
                credits = line[-1]
    file.write(f"{course}, {credits} credits\n======================================\n")
    file.write(f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}\n")
    for id,name in dic1.items():    
        file.write(f"{name:<30}{dic5[id]:<10}{int(dic2[id]):<10}{dic3[id]:<10}{int(dic6[id]):<10}{dic4[id]:<10}\n")
with open('results.csv','w') as file:
    for id,name in dic1.items():    
        file.write(f"{id};{name};{dic4[id]}\n")

#print(f"{'name':<30}{'exec_nbr':<10}{'exec_pts.':<10}{'exm_pts.':<10}{'tot_pts.':<10}{'grade':<10}")
#for id,name in dic1.items():    
#        print(f"{name:<30}{dic5[id]:<10}{int(dic2[id]):<10}{dic3[id]:<10}{int(dic6[id]):<10}{dic4[id]:<10}")

print("Results written to files results.txt and results.csv")



