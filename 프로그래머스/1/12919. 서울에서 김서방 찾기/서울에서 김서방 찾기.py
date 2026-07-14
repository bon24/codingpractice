def solution(seoul):
    answer = ''
    idx = [i for i,v in enumerate(seoul) if v=='Kim']
    return f'김서방은 {idx[0]}에 있다'