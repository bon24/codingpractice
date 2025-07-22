def solution(arr, query):
    # answer = []
    for i in range(len(query)):
        if i%2==0:
            arr=arr[:query[i]+1]
        else:
            arr=arr[query[i]:]
        # if i%2==0:
        #     for j in range(len(arr)-i-1):
        #         arr.pop()
        # else:  
        #     for j in range(i):
        #         arr.pop(j)
    return arr