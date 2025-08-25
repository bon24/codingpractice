def solution(babbling):
    answer = 0
    check=[]
    say = ["aya", "ye", "woo", "ma"]
    for baby in babbling:
        for can in say:
            if can in baby:
                for i in say:
                    baby = baby.replace(i," ")
                check.append(baby)
    for i in range(len(check)):
        check[i]=check[i].replace(" ","")
    for i in check:
        if i=="":
            answer+=1
    return answer