
def contFrac(N):
    import math
    cf=[]
    while True:
        cf.append(int(N))
        f = N - N//1
        if f < 0.0001:  # or whatever precision you consider close enough to 0
            break
        N = 1/f
        if(math.ceil(N)-N<0.0001):
            N=round(N)
    return cf


def convergents(cf):
    from fractions import Fraction 
    c=[] 
    cv=[]
    
    for i in range(len(cf)):
        c.append(cf[i])
        for j in range(i-1,-1,-1):
            c[i] = 1/c[i]+ cf[j]
        cv.append(Fraction(c[i]).limit_denominator(10000))
    return cv
