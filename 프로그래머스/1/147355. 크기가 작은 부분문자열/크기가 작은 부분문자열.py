def solution(t, p):
    answer = 0
    n = list(t)
    
    for i in range(len(n)-len(p)+1):
        num = ''.join(n[i:i+len(p)])

        if int(num)<= int(p):
            answer+=1
    return answer 
