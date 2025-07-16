def solution(my_string, index_list):
    old_word = list(my_string)
    new_word=[]
    for i in index_list:
        new_word.append(old_word[i])
    answer = ''.join(new_word)
    return answer