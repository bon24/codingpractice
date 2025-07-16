def solution(my_string, n):
    string = list(my_string)
    new = []
    answer = ""
    answer += my_string[len(string)-n:len(string)]
    return answer