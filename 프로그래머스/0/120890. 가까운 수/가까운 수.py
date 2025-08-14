def solution(array, n):
    num=[]
    answer=abs(n-array[0])
    for i in  array:
        if abs(n-i)<answer:
            answer = abs(n-i)
    for i in array:
        if answer == abs(n-i):
            num.append(i)
    
    return min(num)