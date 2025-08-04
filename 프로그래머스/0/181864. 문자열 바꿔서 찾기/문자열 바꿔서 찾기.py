def solution(myString, pat):
    a = list(pat)
    for i in range(len(a)):
        if a[i]=="A":
            a[i]="B"
        elif a[i]=="B":
            a[i]="A"
    pata = ''.join(a)
    if pata in myString:
        return 1
    
    return 0