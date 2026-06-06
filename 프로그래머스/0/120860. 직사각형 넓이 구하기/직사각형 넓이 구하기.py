def solution(dots):
    a =[]
    b =[]
    for i,v in dots:
        a.append(i)
        b.append(v)
    a=sorted(list(set(a)))
    b=sorted(list(set(b)))
    answer = abs(a[0]-a[1])*abs(b[0]-b[1])
    return answer