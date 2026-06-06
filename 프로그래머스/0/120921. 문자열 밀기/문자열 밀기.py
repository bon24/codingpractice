def solution(A, B):
    A = list(A)
    result=-1
    if ''.join(A) == B:
            return 0
    for i in range(0,len(A)+1):
        A.insert(0,A.pop())
        if ''.join(A) ==B:
            return i+1
    return result
            
            
            
