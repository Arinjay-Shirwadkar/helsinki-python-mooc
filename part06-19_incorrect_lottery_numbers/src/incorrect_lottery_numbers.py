#1 and 39 inclusive.
def filter_incorrect():

    with open("lottery_numbers.csv") as file:
        with open('correct_numbers.csv','w') as file2:
            for line in file:
                hash =[0]*40
                temp = line
                line = line[5:]
                line = line.strip()
                ind = line.find(';')
                week_no = line[:ind]
                line = line[ind+1:]
                nums = line.split(',')
                if len(nums)!=7 or (not week_no.isnumeric()):
                    continue
                flag=1
                for num in nums:
                    if not num.isnumeric() or int(num)<1 or int(num)>39 or hash[int(num)]!=0:
                        flag=0
                        break
                    hash[int(num)]+=1
                if flag==1:
                    file2.write(temp)
    
