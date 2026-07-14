def solution(left, right):
    answer = 0
    lst = [i for i in range(left,right+1)]
    for num in lst:
        div=0
        for j in range(1,num+1):
            if num%j==0:
                div+=1
        if div %2 ==0:
            answer+=num
        else:
            answer-=num
    return answer