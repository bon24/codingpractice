def solution(my_string, overwrite_string, s):
    my = list(my_string)
    over = list(overwrite_string)
    for i in range(len(over)):
        my[i+s] = over[i]
    answer = ''.join(my)
    return answer
