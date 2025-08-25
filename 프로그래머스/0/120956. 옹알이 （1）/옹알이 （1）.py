def solution(babbling):
    answer = 0
    check=[]
    say = ["aya", "ye", "woo", "ma"]
    for baby in babbling:
        for can in say:
            baby = baby.replace(can," ")
        if baby.strip()=="":
            answer+=1
  
    return answer