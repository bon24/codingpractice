def solution(num, total):
    answer = []
    n = [i for i in range(-1000,1001)]
    i=0
    while True:
        if sum(n[i:i+num]) == total:
            return n[i:i+num]
            break
        i+=1
