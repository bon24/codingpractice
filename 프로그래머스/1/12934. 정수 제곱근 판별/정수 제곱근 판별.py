import math
def solution(n):
    answer = 0
    for i in range(1,int(math.sqrt(n))+1):
        if i*i == n:
            return (i+1)*(i+1)
    return -1
    
    