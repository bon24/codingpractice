def solution(s):
    lst = []
    # lst.append(s[0])
    # s=s[1:]
    for i in s:
        if len(lst)==0:
            lst.append(i)
        elif lst[len(lst)-1] == i:
            lst.pop()
        else:
            lst.append(i)
    if len(lst)==0:
        return 1
    return 0
        
