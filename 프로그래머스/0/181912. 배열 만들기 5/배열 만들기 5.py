def solution(intStrs, k, s, l):
    list_num=[]
    
    for i in intStrs:
        num=""
        for j in range(l):
            num+=i[s+j]
        if int(num) > k:
            list_num.append(int(num))
    return list_num