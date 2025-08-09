def solution(order):
    num=["3","6","9"]
    answer = 0
    order=list(str(order))
    for i in order:
        if i in num:
            answer+=1
    return answer