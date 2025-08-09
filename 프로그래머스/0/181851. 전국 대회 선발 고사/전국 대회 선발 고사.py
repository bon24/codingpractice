def solution(ran, attendance):
    dic = dict(zip(ran,attendance))
    dic = dict(sorted(dic.items()))
    rank=[]
    for k,v in dic.items():
        if len(rank)<3:
            if v==True:
                rank.append(k)
        else:
            break
    for i in range(len(rank)):
        rank[i] = ran.index(rank[i])
    return 10000*rank[0] + 100*rank[1] +rank[2]
