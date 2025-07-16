def solution(my_string, queries):
    
    string = list(my_string)
    for s,e in queries:
        for i in range(int((e-s+1)/2)):
            string[s+i],string[e-i] = string[e-i],string[s+i]
    answer = ''.join(string)
    return answer
