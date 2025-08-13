def solution(strArr):
    lst =[0]*30
    answer = 0
    for i in strArr:
        lst[len(i)-1]+=1
    answer = max(lst)
    return answer