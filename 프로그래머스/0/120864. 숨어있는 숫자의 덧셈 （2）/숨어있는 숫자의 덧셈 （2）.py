def solution(my_string):
    answer = 0
    i=0
    # for i in range(len(my_string)):
    while i<len(my_string):
        if my_string[i].isdigit():
            idx = i
            while idx < len(my_string) and my_string[idx].isdigit():
                idx+=1
            answer+=int(my_string[i:idx])
            i = idx
        else:
            i+=1
    return answer