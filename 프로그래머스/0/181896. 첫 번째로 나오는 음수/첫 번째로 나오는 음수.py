def solution(num_list):
    answer = -1
    # i=0
    # while i<len(num_list):
    #     if num_list[i] <0:
    #         answer=i
    #         break
    #     else:
    #         i+=1
    for i in range(len(num_list)):
        if num_list[i]<0:
            return i
            
    return answer