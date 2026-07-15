def solution(d, budget):
    answer = 0
    m=0
    d = sorted(d)
    for i in range(len(d)):
        m+=d[i]
        if sum(d) <= budget:
            return len(d)
        if budget<m:
            return i
    # for i in range(len(d)):
    #     budget-=d[i]
    #     if budget >=0:
    #         answer+=1
    # return answer
