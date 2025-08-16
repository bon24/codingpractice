def solution(id_pw, db):
    answer = ''
    iid,pw = id_pw[0],id_pw[1]
    for i,p in db:
        if iid == i and pw == p:
            answer = "login"
            break
        else:
            if iid ==i and pw != p:
                answer="wrong pw"
                break
            else:
                answer = "fail"
    return answer