def solution(sides):
    line = 0
    answer=0
    while True:
        line+=1
        sides.append(line)
        side = sorted(sides)
        if side[2] < side[0]+side[1]:
            answer+=1
            
        elif line >= side[2] and side[2] >= side[0]+side[1] :
            break
        sides.pop()
    return answer

            