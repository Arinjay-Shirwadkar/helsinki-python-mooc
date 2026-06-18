def anagrams(s1 : str,s2 : str):
    if len(s1)!=len(s2):
        return False
    hash1 = []
    hash2 = []
    for i in range(26):
        hash1.append(0)
        hash2.append(0)

    for i in range(len(s1)):
        hash1[ord(s1[i])-ord('a')]+=1
        hash2[ord(s2[i])-ord('a')]+=1

    for i in range(26):
        if hash1[i]!=hash2[i]:
            return False
    return True

if __name__=="__main__":
    print(anagrams("trap", "part"))
    print(anagrams("bart", "lisa"))

