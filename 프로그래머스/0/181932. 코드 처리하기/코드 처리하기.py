def solution(code):
    list_code = list(code)
    ret = []
    mode = 0
    for i in range(len(list_code)):
        if mode == 0:
            if list_code[i] != "1":
                if i%2==0:
                    ret.append(list_code[i])
            else:
                mode=1
        elif mode == 1 :
            if list_code[i] != "1":
                if i%2==1:
                    ret.append(list_code[i])
            else:
                mode=0
    ret_word = ''.join(ret)
    if ret_word == '':
        return "EMPTY"
    return ret_word
    
    