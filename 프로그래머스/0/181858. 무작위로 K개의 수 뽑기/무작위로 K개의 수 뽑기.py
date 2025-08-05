def solution(arr, k):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if len(answer)<k:
            if arr[i] not in answer:
                answer.append(arr[i])
                
    if len(answer)<k:
        for i in range(len(answer),k):
            answer.append(-1)
    return answer