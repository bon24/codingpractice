def solution(arr):
    answer = []
    a=-1
    for i in range(len(arr)):
        if arr[i]==2:
            a=i
            break
    for i in range(len(arr)-1,-1,-1):
        if arr[i]==2:
            b=i
            break
    if a==-1:
        answer.append(-1)
    else:
        answer = arr[a:b+1]
    return answer