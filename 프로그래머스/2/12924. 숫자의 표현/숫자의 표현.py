def solution(n):
    answer = 0
    i=0
    while i<=n:
        i+=1 
        num=0
        for j in range(i,n+1):
            num+=j
            if num==n:
                answer+=1
                break
            if num>n:
                break
    return answer