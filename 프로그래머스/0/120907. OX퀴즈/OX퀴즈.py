def solution(quiz):
    answer = []
    
    for i in range(len(quiz)):
        poly=[]
        poly=quiz[i].split()

        if poly[1] == '+' :
            poly.append(int(poly[0])+int(poly[2]))
        elif poly[1] == '-':
            poly.append(int(poly[0])-int(poly[2]))
        if int(poly[4]) == poly[5]:
            answer.append("O")
        else:
            answer.append("X")
    return answer