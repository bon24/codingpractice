def solution(price, money, count):
    answer = 0
    answer = sum([price * i for i in range(1,count+1)])
    if answer - money > 0 :
        return answer - money 
    else:
        return 0 
