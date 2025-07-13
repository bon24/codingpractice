def solution(num_list):
    answer = 0
    add =1
    for i in range(len(num_list)):
        answer += num_list[i]
        add*=num_list[i]
    if add < answer**2:
        return 1
    else:
        return 0