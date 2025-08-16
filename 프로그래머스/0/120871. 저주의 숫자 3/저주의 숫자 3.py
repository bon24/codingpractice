def solution(n):
    answer = 0
    no_three = [] 
    num = 1
    while len(no_three) < n :
        if num % 3!=0 and "3" not in str(num):
            no_three.append(num)
        num+=1
    answer = no_three.pop()
    return answer