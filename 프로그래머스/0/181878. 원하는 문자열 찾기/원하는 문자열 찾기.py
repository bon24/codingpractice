def solution(myString, pat):
    answer = 0
    string = myString.upper()
    find = pat.upper()
    if find in string:
        return 1
    return answer