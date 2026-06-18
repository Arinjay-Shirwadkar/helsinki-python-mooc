def everything_reversed(lis):
    rev_lis = lis[::-1]
    print(rev_lis)
    for i in range(len(rev_lis)):
        rev_lis[i] = rev_lis[i][::-1]
    return rev_lis

if __name__=="__main__":
    print(everything_reversed(["Hello","There"]))