def solution(common):
#     answer = 0
    
#     if (common[1] - common[0]) ==  (common[2] - common[1]):
#         num = common[1] - common[0]
#         answer = common[-1] + num
#     if (common[1] // common[0]) == (common[2] // common[1]):
#         num = common[1] // common[0]
#         answer = common[-1]*num
    answer = 0
    if (common[2]-common[1])==(common[1]-common[0]):
        return common[-1]+(common[1]-common[0])
    else:
        return common[-1]*((common[2]-common[1])//(common[1]-common[0]))
    return answer
