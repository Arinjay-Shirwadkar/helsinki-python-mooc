def longest_series_of_neighbours(lis):
    longest=1
    streak=1 
    for i in range(1,len(lis)):
        if not abs(lis[i-1]-lis[i])==1:
            
            if streak>longest:
                longest=streak
            streak=1

        else:
            streak+=1
            if i == len(lis)-1:
                if streak>longest:
                 longest=streak

    return longest
        

        
            
