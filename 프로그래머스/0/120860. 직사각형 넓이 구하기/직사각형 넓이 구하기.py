def solution(dots):
    answer = 1
    side = []
    for i in range(len(dots)-1):
        if abs(dots[i][0] - dots[i+1][0])>0:
            side.append(abs(dots[i][0] - dots[i+1][0]))
        if abs(dots[i][1] - dots[i+1][1])>0:
            side.append(abs(dots[i][1] - dots[i+1][1]))
    side = list(set(side))
    if len(side) == 1:
        answer  = side[0]**2
    else:
        answer = side[0] * side[1]
    return answer