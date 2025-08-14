def solution(s):
    num = s.split()
    answer = 0
    for i in range(len(num)):
        if num[i] == 'Z':
            answer= answer - int(num[i-1])
        else:
            answer+=int(num[i])
    return answer