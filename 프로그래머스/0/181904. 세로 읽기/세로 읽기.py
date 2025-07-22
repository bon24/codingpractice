def solution(my_string, m, c):
    i=0
    list_word=[]
    while i<len(my_string):
        list_word.append(my_string[i:i+m])
        i+=m
    answer = ''
    for i in range(len(list_word)):
        answer+=list_word[i][c-1]
    return answer

    