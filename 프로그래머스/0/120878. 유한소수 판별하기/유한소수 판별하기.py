def solution(a, b):
    num=1
    for i in range(2,b+1):
        if a%i==0 and b%i==0:
            num=i
    b//=num   
    divisor = 2
    if b==1:
        return 1
    while b > 1:
        if b % divisor == 0:
            if divisor !=2 and divisor!=5:
                return 2
            b //= divisor
        else:
            divisor += 1
    return 1