def solution(n_str):
    answer = ''
    n = list(n_str)
    for i in range(len(n)):
        if n[i] != "0" :
            idx=i
            break
    print(idx)
    answer = ''.join(n[idx:])
    return answer