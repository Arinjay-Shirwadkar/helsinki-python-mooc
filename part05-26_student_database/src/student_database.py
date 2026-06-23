def add_student(students:dict,stud:str):
    students[stud]=[]
    students[stud].append(("no completed courses"))

def print_student(students:dict,stud:str):
    if stud in students:
        print(stud+":")
        if ("no completed courses") in students[stud]:
            print(" no completed courses")
        else:
            print("",len(students[stud]),"completed courses:")
            avg=0
            for course in students[stud]:
                print(" ",course[0],course[1])
                avg+=course[1]

            print(" average grade",(avg)/len(students[stud]))
                
    else:
        print(stud+": no such person in the database")

def summary(students:dict):
    print("students",len(students))
    maxCourses=0
    maxGrade=0
    achiever=""
    brilliant=""
    
    for stud,courses in students.items():
        avg=0
        if len(courses)>maxCourses:
            maxCourses=len(courses)
            achiever = stud
        for course in courses:
            avg+=course[1]
        avg=avg/len(courses)
        if avg>maxGrade:
            maxGrade=avg
            brilliant=stud
    print("most courses completed",maxCourses,""+achiever)
    print("best average grade",maxGrade,""+brilliant)


def add_course(students:dict,stud:str,tup:tuple):
    if tup[1]==0:
        return
    if ("no completed courses") in students[stud]:
        students[stud].pop()
    for i in range(0,len(students[stud])):
        if students[stud][i][0]==tup[0]:
            if students[stud][i][1]>=tup[1]:
                return
            else:
                students[stud].remove(students[stud][i])
                students[stud].append(tup)
                return                  

    students[stud].append(tup)



if __name__=="__main__":

    students = {}
    add_student(students, "Peter")
    add_student(students, "Eliza")
    add_course(students, "Peter", ("Data Structures and Algorithms", 1))
    add_course(students, "Peter", ("Introduction to Programming", 1))
    add_course(students, "Peter", ("Advanced Course in Programming", 1))
    add_course(students, "Eliza", ("Introduction to Programming", 5))
    add_course(students, "Eliza", ("Introduction to Computer Science", 4))
    summary(students)   