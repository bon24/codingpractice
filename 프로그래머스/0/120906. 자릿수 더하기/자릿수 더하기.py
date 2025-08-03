def solution(n):
    a = str(n)
    answer = 0
    lst = list(a)
    for i in lst:
        answer+=int(i)
    
    return answer