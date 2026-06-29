import fractions

def fractionate(n):
    lis = []
    for i in range(1,n+1):
        lis.append(fractions.Fraction(1,n))
    return lis