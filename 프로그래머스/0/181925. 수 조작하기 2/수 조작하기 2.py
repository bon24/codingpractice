def solution(numLog):
    dic = {"w":1 , "s":-1,"d":10,"a":-10}
    result=""
    for i in range(1,len(numLog)):
        for k,v in dic.items():
            if v==numLog[i]-numLog[i-1]:
                result+=k
    return result