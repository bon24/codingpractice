def solution(myString, pat):
    answer=""
    idx = myString.rfind(pat)
    answer=myString[:idx+len(pat)]
    # for i in range(idx+len(pat)):
    #     answer +=a[i]
    return answer