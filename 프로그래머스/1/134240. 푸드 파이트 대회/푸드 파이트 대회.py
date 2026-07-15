def solution(food):
    line = 0
    answer = ''
    food = food[1:]
    for i,v in enumerate(food):
        answer+=(str(i+1)*(v//2))
    answer = answer + '0' + answer[::-1]
            
    return answer

    