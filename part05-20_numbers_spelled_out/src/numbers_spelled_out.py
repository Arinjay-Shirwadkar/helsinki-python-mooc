def dict_of_numbers():
    dic={}
    units={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve'}
    tens={2:"twen",3:"thir",4:"four",5:"fif",6:"six",7:"seven",8:"eigh",9:"nine"}
    
    for i in range(0,100):
        if i<=12:
         dic[i]=units[i]
        elif i<20:
           u=i%10
           s1=tens[u]
           dic[i]=s1+'teen'
        else:
           t=i//10
           u=i%10
           s1=tens[t]
           if u!=0:
              s2=units[u]
              dic[i]=s1+'ty-'+s2
           else:
              dic[i]=s1+'ty'
    return dic
if __name__=="__main__":
   print(dict_of_numbers())