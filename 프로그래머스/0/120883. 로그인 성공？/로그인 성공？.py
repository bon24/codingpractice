def solution(id_pw, db):
    answer=''
    for v in db:
        if id_pw[0] in v:
            if id_pw[1] == v[1]:
                answer='login'
                break
            else:
                answer='wrong pw'
                break
        else:
            answer='fail'
    return answer