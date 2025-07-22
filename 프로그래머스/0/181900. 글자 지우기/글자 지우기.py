def solution(my_string, indices):
    word = list(my_string)
    for i in indices:
        word[i] = ''
    answer = ''.join(word)
    return answer