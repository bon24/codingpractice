def solution(x1, x2, x3, x4): 
# ^둘다 true true >이건 하나만 true여도 true
    # answer = True
    if (x1==True or x2==True) and  (x3==True or x4==True) :
        answer = True
    else:
        answer= False
    return answer