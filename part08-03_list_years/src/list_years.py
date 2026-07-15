# Write your solution here
# Remember the import statement
# from datetime import date

from datetime import date


def list_years(dates: list):
    lis =[]
    for dat in dates:
        lis.append(dat.year)
    
    for i in range(0,len(lis)-1):
        for j in range(0,len(lis)-i-1):
            if lis[j+1]<lis[j]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
    
    
    return lis

if __name__=="__main__":
    date1 = date(2019, 2, 3)
    date2 = date(2006, 10, 10)
    date3 = date(1993, 5, 9)

    years = list_years([date1, date2, date3])
    print(years)
