def solution(age):
    dic = {"a":"0","b":"1","c":"2","d":"3","e":"4","f":"5","g":"6",
           "h":"7","i":"8","j":"9"}
    answer = ''
    age = list(str(age))
    for k,v in dic.items():
        for i in range(len(age)):
            if age[i]==v:
                age[i]=k
    answer = "".join(age)
    return answer