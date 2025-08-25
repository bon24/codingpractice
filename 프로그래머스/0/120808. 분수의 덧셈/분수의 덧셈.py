def solution(numer1, denom1, numer2, denom2):
    answer = []
    numer1 *= denom2
    numer2 *= denom1
    numer = numer1+numer2
    denom = denom1*denom2
    m = max(numer,denom)
    divisor = [i for i in range(2,m+1) if m%i==0]
    for i in divisor:
        if numer%i==0 and denom%i==0:
            while numer%i==0 and denom%i==0:
                numer//=i
                denom//=i
    answer = [numer,denom]
    return answer