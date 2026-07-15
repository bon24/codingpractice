def solution(n, m):
    answer = []
    num=max(n,m)
    for i in range(min(n,m),0,-1):
        if n%i==0 and m%i==0:
            answer.append(i)
            break
    while True:
        if num % n ==0 and num%m==0:
            answer.append(num)
            break
        num+=1
    return answer