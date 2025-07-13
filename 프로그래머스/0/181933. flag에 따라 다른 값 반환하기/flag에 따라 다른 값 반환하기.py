def solution(a, b, flag):
    answer = 0
    if bool(flag) == True:
        answer = a+b
    else:
        answer = a-b
    return answer