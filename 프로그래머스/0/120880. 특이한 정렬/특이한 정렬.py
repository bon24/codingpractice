def solution(numlist, n):
    answer = []
    minus = map(lambda x: abs(x-n),numlist)
    dic = dict(zip(numlist,minus))
    a = list(sorted(dic.items(), key=lambda x: (x[1], -x[0])))
    for i,v in a:
        answer.append(i)
    
    return answer