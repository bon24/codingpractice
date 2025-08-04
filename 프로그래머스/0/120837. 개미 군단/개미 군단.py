def solution(hp):
    answer = 0
    while hp>=3:
        if hp>=5 :
            
            answer += hp//5
            hp = hp%5
        if 3<=hp<5:
            
            answer += hp//3
            hp = hp%3
    answer += hp
    return answer

# 장군개미 -5
# 병정개미 - 3
# 일개미 -1