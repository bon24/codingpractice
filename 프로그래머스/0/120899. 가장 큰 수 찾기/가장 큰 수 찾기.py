def solution(array):
    answer = []
    for i,v in enumerate(array):
        if v==max(array):
            answer=[v,i]
    return answer