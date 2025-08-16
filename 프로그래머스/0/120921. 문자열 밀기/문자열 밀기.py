def solution(A, B):
    A = list(A)
    answer = 0
    if ''.join(A) == B:
        return 0
    
    while answer<len(B):
        answer+=1
        A.insert(0,A.pop())
        if B == ''.join(A):
            break
    if answer >= len(B):
        return -1
    else:
        return answer
            
            
            
            
    # for i in range(len(A)-1,0,-1):
    #     A.insert(0,A[i])
    #     print(A)
    #     print(''.join(A[:len(B)]))
    #     if B == ''.join(A[:len(B)]):
    #         chance.append(i)
    # if len(chance)==0:
    #     return -1
    # else:
    #     return min(chance)