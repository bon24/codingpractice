def solution(brown, yellow):
    divisor=[]
    answer=[]
    for i in range(1,yellow+1):
        if yellow%i==0:
            divisor.append(i)

    if len(divisor)%2==0:
        idx = (len(divisor)//2)-1
        for i in range(idx+1):
            bro = 2*(divisor[i]+divisor[len(divisor)-i-1])+4
            if brown == bro:
                answer.append(divisor[len(divisor)-i-1]+2)
                answer.append(divisor[i]+2)
                break
            
    else:
        answer.append(divisor[len(divisor)//2]+2)
        answer.append(divisor[len(divisor)//2]+2)
    return answer
                
            
            
    # n = brown + yellow
    # divisor = []
    # answer = []
    # for i in range(1,n+1):
    #     if n%i==0:
    #         divisor.append(i)
    # if len(divisor)%2==0:
    #     answer.append(divisor[len(divisor)//2])
    #     answer.append(divisor[(len(divisor)//2)-1])
    # else:
    #     answer.append(divisor[len(divisor)//2])
    #     answer.append(divisor[len(divisor)//2])
    # return answer
   