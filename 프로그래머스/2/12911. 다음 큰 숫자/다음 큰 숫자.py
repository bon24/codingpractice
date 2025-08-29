def solution(n):
    answer = 0
    num = bin(n)[2:]
    num = num.count("1")
    while True:
        n+=1
        num1 = bin(n)[2:]
        num1 = num1.count("1")
        if num == num1:
            return n
    return answer