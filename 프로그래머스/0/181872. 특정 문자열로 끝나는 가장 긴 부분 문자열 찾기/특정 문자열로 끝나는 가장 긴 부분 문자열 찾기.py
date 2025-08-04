def solution(myString, pat):
    answer=""
    idx = myString.rfind(pat)
    a = list(myString)
    for i in range(idx+len(pat)):
        answer +=a[i]
    return answer