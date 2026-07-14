def solution(arr):
    if len(arr) ==1 :
        return [-1]
    answer = []
    num = min(arr)
    for i in arr:
        if i!=num:
            answer.append(i)
    
    return answer