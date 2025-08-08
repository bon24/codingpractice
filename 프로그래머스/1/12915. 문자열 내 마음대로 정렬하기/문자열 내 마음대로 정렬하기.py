def solution(strings, n):
# 인덱스 문자 + strings요소 담기
    lst=[]
    answer=[]
    for i in strings:
        lst.append(i[n]+i)
    answer = sorted(lst)
    
    for i in range(len(answer)):
        answer[i] = answer[i][1:]
    # for i in strings:
    #     lst.append(i[n])
    # strings=sorted(strings)
    # lst = sorted(lst)
    # i=0
    # while i<3:
    #     for j in strings:
    #         if lst[i] ==j[n]:
    #             if j not in answer:
    #                 answer.append(j)
    #                 i+=1
    return answer
        
    
    
    
    
    