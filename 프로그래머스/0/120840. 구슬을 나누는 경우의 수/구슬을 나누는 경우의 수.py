def fac(n):
    i=n-1
    while i>1:
        n=n*i
        i=i-1
    return n
def solution(balls, share):
    if balls == share:
        return 1
    else:
        answer = fac(balls)/(fac(balls-share)*fac(share))
    return answer