inp = input("Exam points and exercises completed: ")
grade = []
for i in range(6):
    grade.append(0)

numStudents=0
runSum=0

while inp!="":
    numStudents+=1
    for i in range(len(inp)):
        if inp[i]==' ':
            break
    exam = int(inp[:i])
    exer = int(inp[i+1:])
    currSum=exam+exer//10
    runSum+=currSum
    if exam<10 or currSum<=14:
        grade[0]+=1
    elif currSum<17:
        grade[1]+=1
    elif currSum<=20:
        grade[2]+=1
    elif currSum<=23:
        grade[3]+=1
    elif currSum<=27:
        grade[4]+=1
    elif currSum<=30:
        grade[5]+=1

    inp = input("Exam points and exercises completed: ")

print(f"Statistics:\nPoints average: {(runSum/numStudents):.1f}\nPass percentage: {((grade[1]+grade[2]+grade[3]+grade[4]+grade[5])*100/numStudents):.1f}\nGrade distribution:")

for i in range(5,-1,-1):
    print(f" {i}: {grade[i]*"*"}")


