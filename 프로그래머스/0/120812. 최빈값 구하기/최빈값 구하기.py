def solution(array):
    arr = set(sorted(array))
    count = list(map(lambda x: array.count(x) , arr))
    dic = dict(zip(arr,count))
    
    answer = []
    for k,v in dic.items():
        if v == max(count):
            answer.append(k)
    if len(answer) != 1:
        return -1
    else:
        return answer[0]