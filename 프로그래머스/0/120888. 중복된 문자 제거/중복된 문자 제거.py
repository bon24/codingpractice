def solution(my_string):
    new =[]
    for i in my_string:
        if i not in new:
            new.append(i)
    answer = ''.join(new)
    return answer