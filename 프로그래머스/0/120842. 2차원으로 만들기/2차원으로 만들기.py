def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):   # 0부터 n씩 증가
        answer.append(num_list[i:i+n])     # i부터 i+n까지 잘라서 추가
    return answer