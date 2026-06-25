import math

def read_file(filename):
    lis=[]
    listinlis =[]
    once=1
    with open(filename) as file:
        for line in file:
            if once==1:
                once=0
                continue
            line = line.strip()
            listinlis = line.split(";")
            lis.append(listinlis)
    return lis

def get_station_data(filename: str):
    
    dic={}
    stations = read_file(filename)
    for station in stations:
        dic[station[3]] = (float(station[0]),float(station[1]))
    
    return dic

def distance(stations: dict, station1: str, station2: str):
    longitude1= float(stations[station1][0])
    longitude2= float(stations[station2][0])
    latitude1= float(stations[station1][1])
    latitude2= float(stations[station2][1])
    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km

def greatest_distance(stations: dict):
    distances = [] #list of tuples, this shall be. We must fill it first
    for station1 in stations:
        for station2 in stations:
            if station2==station1:
                continue
            distances.append((station1,station2,distance(stations, station1, station2)))
    max=0
    tup=()
    for distance_instance in distances:
        if distance_instance[2]>max:
            max=distance_instance[2]
            tup=distance_instance
    return tup

if __name__=="__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)