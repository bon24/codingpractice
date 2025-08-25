def solution(lines):
    answer = 0
    line1 = []
    line2 = []
    line3 = []
    check = []
    for j in range(lines[0][0],lines[0][1]):
        line1.append([j,j+1])
    for j in range(lines[1][0],lines[1][1]):
        line2.append([j,j+1])
    for j in range(lines[2][0],lines[2][1]):
        line3.append([j,j+1])
        
    for i in line1:
        if i in line2 and i not in check:
            check.append(i)
            answer+=1
            print(i,"1")
    for i in line2:
        if i in line3 and i not in check:
            check.append(i)
            answer+=1
            print(i,"2")
    for i in line3:
        if i in line1 and i not in check:
            check.append(i)
            answer+=1
            print(i,"3")
    return answer

# [3,5] [3,9] 4
# [3,9] [1,5] 4
# [1,5]

# [3,5]

# []