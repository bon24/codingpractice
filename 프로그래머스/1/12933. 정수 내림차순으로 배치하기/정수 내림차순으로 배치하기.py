def solution(n):
    answer = 0
    n = list(str(n))
    num = sorted(n,reverse=True)
    answer = int(''.join(num))
    return answer