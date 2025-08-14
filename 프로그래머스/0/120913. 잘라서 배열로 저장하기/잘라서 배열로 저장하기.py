def solution(my_str, n):
    my = list(my_str)
    answer = []
    for i in range(0,len(my),n):
        answer.append(my_str[i:i+n])
    return answer