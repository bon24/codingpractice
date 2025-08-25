def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    num = list(zip(A,B))
    for i in num:
        answer += (i[0]*i[1])
    return answer