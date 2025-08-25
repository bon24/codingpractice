def solution(s):
    stack = []
    for i in s:
        if len(stack)==0:
            stack.append(i)
        else:
            if i == "(":
                stack.append(i)
            else:
                stack[len(stack)-1] == ")"
                stack.pop()
    if len(stack)==0:
        return True
    return False

