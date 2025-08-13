def solution(s):
    s=sorted(s)
    answer=''
    for i in s:
        scopy = s.copy()
        scopy.remove(i)
        if i not in scopy:
            answer+=i
    return answer