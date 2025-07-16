def solution(my_string, is_suffix):
    answer = 0
    word = []
    for i in range(len(my_string)):
        word.append(my_string[i::])
    word.sort()
    for i in word:
        if i==is_suffix:
            answer = 1
    return answer