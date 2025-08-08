def solution(n):
    answer = ''
    s = "수"
    s1="박"
    for i in range(int(n/2)):
        answer+=s
        answer+=s1
    if n%2==1:
        answer+=s
    return answer