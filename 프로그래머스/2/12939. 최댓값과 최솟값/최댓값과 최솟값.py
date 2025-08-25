def solution(s):
    answer = ''
    s = s.split()
    lst = list(map(int,s))
    maxx = str(max(lst))
    minn = str(min(lst))
    answer = f"{minn} {maxx}"
    
    return answer