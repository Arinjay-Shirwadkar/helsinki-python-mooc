def longest(strs):
    l=0
    for s in strs:
        if len(s)>l:
            l=len(s)
            longest=s
    return longest

if __name__=="__main__":
    print(longest(["Hello", "World", "Stupide editor"]))