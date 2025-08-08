def solution(s):
    
    answer = []
    string = list(s)
    for i in range(len(string)):
        a=[]
        
        for j in range(i+1):
            if string[i] == string[j]:
                if i!=j:
                    a.append(i-j)
        if len(a)==0:
            answer.append(-1)
        else:
            answer.append(min(a))
    
    return answer