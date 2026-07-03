import json
import urllib.request

def retrieve_all():
    my_req = urllib.request.urlopen('https://studies.cs.helsinki.fi/stats-mock/api/courses')
    content = json.loads(my_req.read())
    lis = []
    for element in content:
        if not element['enabled']:
            continue
        lis.append((element['fullName'],element['name'],element['year'],sum(element['exercises'])))
    return lis

def retrieve_course(coname):
    link = f'https://studies.cs.helsinki.fi/stats-mock/api/courses/{coname}/stats'
    req = urllib.request.urlopen(link)
    content = json.loads(req.read())
    weeks = len(content)
    students = 0
    hours = 0
    exercises = 0
    for one in content:
        if content[one]['students']>students:
            students= content[one]['students']
        hours+= content[one]['hour_total']
        exercises+= content[one]['exercise_total']
    hours_average = hours//students
    exercises_average = exercises//students
    dic = {
    'weeks': weeks,
    'students': students,
    'hours': hours,
    'hours_average': hours_average,
    'exercises': exercises,
    'exercises_average': exercises_average
            }
    return dic


if __name__ == "__main__":
    print(retrieve_all())
    print(retrieve_course('docker2019'))