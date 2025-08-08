def solution(s):
    answer = ''
    lst=[]
    a=s.split(' ')
    for i in range(len(a)):
        lst = list(a[i])
        for j in range(len(lst)):
            if j%2==0:
                lst[j] = lst[j].upper()
            else:
                lst[j] = lst[j].lower()
        a[i] = ''.join(lst)
    answer = ' '.join(a)
    return answer