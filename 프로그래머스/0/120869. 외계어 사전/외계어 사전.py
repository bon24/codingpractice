def solution(spell, dic):
    answer = 2
    spell = ''.join(sorted(spell))
    new_dic = []

    for word in dic:
        word = ''.join(sorted(word))
        new_dic.append(word)
        for char in new_dic:
            if char == spell:
                return 1
            
    return answer


# def solution(spell, dic):
#     s=''
#     lst = []
#     a=0
#     answer = 2
#     for i in dic:
#         if len(spell) == i:
#             lst.append(i)
#     for i in dic:
#         for j in spell:
#             if j in i:
#                 a+=1
#     if a==len(spell):
#         return 1
#     return 2
    
    