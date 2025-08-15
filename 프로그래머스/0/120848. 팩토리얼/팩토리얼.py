def fac(num):
    i = num-1
    while i>1:
        num=num*(i)
        i=i-1
    return num
def solution(n):
    a = 1
    while True:
        print(fac(a))
        if fac(a)<=n:
            a+=1
        else:
            return a-1
            break
