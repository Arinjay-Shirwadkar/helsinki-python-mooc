def final_points():
    name_to_time = {}
    dic = {} #map student names to dictionaries which map tasks to points
    with open('start_times.csv') as fil:
        for line in fil:
            line = line.strip()
            spline = line.split(';')
            time = spline[1].split(':')
            time[0] = int(time[0])
            time[1] = int(time[1])
            name_to_time[spline[0]] = time
    
    cheaters = []
    with open('submissions.csv') as fil:
        for line in fil:
            line = line.strip()
            spline = line.split(';')
            name = spline[0]
            time = spline[3].split(':')
            task = spline[1]
            points = spline[2]
            time[0] = int(time[0])
            time[1] = int(time[1])
            start_time = name_to_time[name].copy()

            if time[1]<start_time[1]:
                time[0]-=1
                time[1]=time[1] + 60 - start_time[1]
            else:
                time[1] = time[1] - start_time[1]

            if (time[0] - start_time[0]>=3) and (time[1]!=0) and (name not in cheaters):
                continue

            #all that will validate or invalidate a submission
            if name in dic:
                if task in dic[name]:
                    if int(dic[name][task])<int(points):
                        dic[name][task] = points
                else:
                    dic[name][task] = points
            else:
                dic[name] = {task:points}
    finaldic = {}
    for name in dic:
        totalpoints = 0
        for task in dic[name]:
            totalpoints+= int(dic[name][task])
        finaldic[name] = totalpoints

    return finaldic

if __name__ =="__main__":
    print(final_points())