def solution(a, b, c, d):
    nums = [a, b, c, d]

    # 네 개 모두 같은 경우
    if a == b == c == d:
        return 1111 * a

    # 세 개가 같고 하나만 다른 경우
    for x in nums:
        if nums.count(x) == 3:
            for y in nums:
                if x != y:
                    return (10 * x + y) ** 2

    # 두 개씩 같은 값이 나온 경우 (ex. 2,2,4,4)
    pair_values = []
    for x in set(nums):
        if nums.count(x) == 2:
            pair_values.append(x)
    if len(pair_values) == 2:
        p, q = pair_values
        return (p + q) * abs(p - q)

    # 두 개만 같고 나머지 서로 다른 경우 (ex. 2,2,3,5)
    for x in nums:
        if nums.count(x) == 2:
            others = [n for n in nums if n != x]
            if len(others) == 2 and others[0] != others[1]:
                return others[0] * others[1]

    # 모두 다른 경우
    return min(nums)

