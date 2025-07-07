def solution(a, b):
    sa = str(a)
    sb=str(b)
    answer = max(int(sa+sb),2*a*b)
    return answer