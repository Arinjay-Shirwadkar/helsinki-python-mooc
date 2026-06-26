def find_words(s: str):
    lis =[]
    if '.' in s:
        with open('words.txt') as file:
            for line in file:
                line = line.strip()
                addornot=True
                if len(line)==len(s):
                    for i in range(0,len(line)):
                        if s[i]!='.' and s[i]!=line[i]:
                            addornot=False
                            break
                else:
                    addornot=False
                if addornot==True:
                    lis.append(line)

    elif '*' in s:
        with open('words.txt') as file:
            for line in file:
                line = line.strip()
                addornot=True
                if s[0]=='*':
                    if line.endswith(s[1:]):
                        lis.append(line)
                else:
                    if line.startswith(s[:len(s)-1]):
                        lis.append(line)

    else:
        with open('words.txt') as file:
            for line in file:
                line = line.strip()
                if line==s:
                    lis.append(line)

    return lis

if __name__ == "__main__":
    print(find_words("*yoke"))










