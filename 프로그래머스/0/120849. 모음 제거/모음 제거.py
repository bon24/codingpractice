def solution(my_string):
    
    b=["a","e","i","o","u"]
    answer = ''
    for i in b:
        if i in my_string:
            my_string = my_string.replace(i,"")
    return my_string