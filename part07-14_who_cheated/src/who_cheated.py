def cheaters():
    name_to_time = {}
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
            time[0] = int(time[0])
            time[1] = int(time[1])
            start_time = name_to_time[name].copy()

            if time[1]<start_time[1]:
                time[0]-=1
                time[1]=time[1] + 60 - start_time[1]
            else:
                time[1] = time[1] - start_time[1]

            if (time[0] - start_time[0]>=3) and (time[1]!=0) and (name not in cheaters):
                cheaters.append(name)
    return cheaters

if __name__ =="__main__":
    print(cheaters())