def solution(numbers, direction):
    answer=[]
    if direction =="right":
        answer = numbers.copy()
        answer.insert(0,numbers[len(numbers)-1])        
        answer.pop()
        # for i,v in enumerate(numbers):
        #     answer[len(numbers)-1-i]=v
    else:
        answer = numbers.copy()
        answer.append(numbers[0])
        answer.pop(0)
    return answer
# right >> (len()-1) - index
# left >> 