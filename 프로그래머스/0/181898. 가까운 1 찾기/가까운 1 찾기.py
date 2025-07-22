def solution(arr, idx):
    answer = -1
    while idx<len(arr):
        if arr[idx]==1:
            answer=idx
            break
        else:
            idx+=1
    return answer