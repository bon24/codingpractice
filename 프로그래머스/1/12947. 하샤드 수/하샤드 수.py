def solution(x):
    answer = True
    n = sum([int(i) for i in str(x)])
    if x%n==0:
        return True
    return False