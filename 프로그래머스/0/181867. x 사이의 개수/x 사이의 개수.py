def solution(myString):
    answer = myString.split("x")
    a=[]
    for i in answer:
        a.append(len(i))
    return a