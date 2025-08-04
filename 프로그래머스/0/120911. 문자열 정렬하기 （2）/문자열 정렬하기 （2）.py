def solution(my_string):
    my_string =my_string.lower()
    a=list(my_string)
    
    a.sort()
    
    answer = ''.join(a)
    return answer