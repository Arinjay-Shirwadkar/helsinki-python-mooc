def run(program):
    vars = {}
    for i in range(0,26):
        vars[(chr(i+ord('A')))] = 0
    
    sol = []
    i=0
    while i<len(program):
        line = program[i]
        line = line.split(' ')
        op =line[0]
        if op == 'MOV':
            vars[line[1]] = int(line[2]) if line[2].isdigit() else vars[line[2]]
        elif op == 'ADD':
            vars[line[1]] += int(line[2]) if line[2].isdigit() else vars[line[2]]
        elif op == 'SUB':
            vars[line[1]] -= int(line[2]) if line[2].isdigit() else vars[line[2]]
        elif op == 'MUL':
            vars[line[1]] *= int(line[2]) if line[2].isdigit() else vars[line[2]]
        elif op == 'JUMP':
            line[1] = line[1]+':'
            loc = program.index(line[1])
            i = loc+1
            continue
        elif op == 'IF':
            #5 things in line
            #eg "IF B <= 10 JUMP begin"
            op1 = int(line[1]) if line[1].isdigit() else vars[line[1]]
            op2 = int(line[3]) if line[3].isdigit() else vars[line[3]]
            line[5]=line[5]+':'
            if line[2] == '==':
                
                if op1==op2:
                    loc = program.index(line[5])
                    i = loc+1
                    continue
            elif line[2] == '>=':
                if op1>=op2:
                    loc = program.index(line[5])
                    i = loc+1
                    continue
            elif line[2] == '<=':
                if op1<=op2:
                    loc = program.index(line[5])
                    i = loc+1
                    continue
            elif line[2] == '!=':
                if op1!=op2:
                    loc = program.index(line[5])
                    i = loc+1
                    continue
            elif line[2] == '<':
                if op1<op2:
                    loc = program.index(line[5])
                    i = loc+1
                    continue
            elif line[2] == '>':
                if op1>op2:
                    loc = program.index(line[5])
                    i = loc+1
                    continue
        elif op =='END':
            break
        elif op =='PRINT':
            sol.append(int(line[1]) if line[1].isdigit() else vars[line[1]])
        i+=1
    return sol

if __name__=="__main__":
    program3 = []
    program3.append("MOV A 1")
    program3.append("MOV B 1")
    program3.append("begin:")
    program3.append("PRINT A")
    program3.append("ADD B 1")
    program3.append("MUL A B")
    program3.append("IF B <= 10 JUMP begin")
    program3.append("END")
    result = run(program3)
    print(result)