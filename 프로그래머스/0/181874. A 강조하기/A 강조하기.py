def solution(myString):
    
    lst = list(myString)
    for idx,v in enumerate(lst):
        if v=="a" or v=="A":
            lst[idx]= lst[idx].upper()
        else:
            if lst[idx].isupper():
                lst[idx]=lst[idx].lower()
    answer = ''.join(lst)
    return answer