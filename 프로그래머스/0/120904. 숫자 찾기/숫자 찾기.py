def solution(num, k):
    answer = -1
    if str(k) in str(num):
        return (str(num).find(str(k)))+1
    return answer