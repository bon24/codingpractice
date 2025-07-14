def solution(l, r):
    answer = []
    
    for i in range(l,r+1):
        num = str(i)
        valid = True
        for x in num:
            if int(x)%5!=0:
                valid=False
        if valid:
            answer.append(i)
    if len(answer)==0:
        answer.append(-1)
    return answer