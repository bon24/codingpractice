def solution(myString):
    a=myString.split("x")
    # answer = []
    # for i in a:
    #     if len(i) != 0:
    #         answer.append(i)
    # answer.sort()
    return sorted(i for i in a if len(i)!=0)