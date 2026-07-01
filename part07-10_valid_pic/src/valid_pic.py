from datetime import datetime
#import string

def is_it_valid(pic: str):
    #ddmmyyXyyyz
    if(len(pic)!=11):
        return False
    day = pic[:2]
    month = pic[2:4]
    year = pic[4:6]
    cen =  pic[6]
    z = pic[10]
    if cen=='+':
        cent = 1800
    elif cen=='-':
        cent = 1900
    elif cen=='A':
        cent = 2000
    else:
        return False
    try:
        trythis = datetime(int(year)+cent,int(month), int(day))
    except ValueError:
        #Gotcha, Sucker! What a way to check for correctness, huh?
        return False
    const = '0123456789ABCDEFHJKLMNPRSTUVWXY'
    #print(const)
    #print((int(day + month + year + pic[7:10]))%31)
    #print(const[(int(day + month + year + pic[7:10]))%31])
    #print('0123456789ABCDEFHJKLMNPRSTUVWXY'[21])
    whatitshouldbe = const[(int(day + month + year + pic[7:10]))%31]
    if z!=whatitshouldbe:
        return False
    
    return True


if __name__=="__main__":
    print(is_it_valid("080842-720N"))
