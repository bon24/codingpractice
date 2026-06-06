def solution(n):
    answer=0
    num=1
    three=[]
    while len(three)<n:
        if num%3!=0 and '3' not in str(num):
            three.append(num)
        num+=1
    answer=three.pop()
            
    return answer
    