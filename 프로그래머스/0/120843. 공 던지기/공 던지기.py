def solution(numbers, k):
    answer = 0
    num=[]
    if len(numbers) < k*2:
        numbers*=k
    for i in range(0,k*2,2):
        num.append(numbers[i])
    answer = num.pop()
    return answer