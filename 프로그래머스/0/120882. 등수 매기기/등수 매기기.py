def solution(score):
    mean = list(map(lambda x: sum(x)/2,score))
    answer = [1] * len(mean)
    for i in range(len(mean)):
        for j in range(len(mean)):
            if mean[i] < mean[j]:
                answer[i]+=1
    
    return answer