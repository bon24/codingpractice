def solution(i, j, k):
    answer = 0
    k = str(k)
    for string in range(i,j+1):
        s = list(str(string))
        answer+=s.count(k)
        # if s.count(k):
        #     print(s)
        #     answer+=1
    return answer