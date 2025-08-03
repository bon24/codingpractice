def solution(angle):
    answer = 0
    if angle<90:
        a = 1
    elif angle == 90:
        a=2
    elif angle>=90 and angle<180:
        a=3
    else:
        a=4
    return a