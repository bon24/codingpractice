def solution(my_string, n):
    answer = ''
    a = list(my_string)
    for i in a:
        answer+=i*n
    return answer