def solution(array, commands):
    answer = []
    for idx in commands:
        a=[]
        a = array[idx[0]-1:idx[1]]
        a=sorted(a)
        answer.append(a[idx[2]-1])
    return answer