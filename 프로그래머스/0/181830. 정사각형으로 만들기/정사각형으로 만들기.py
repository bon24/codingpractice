def solution(arr):
    row,col = len(arr[0]),len(arr)
    n = max(row,col)
    answer = [[0]*n for _ in range(n) ]
    for i in range(col):
        for j in range(row):
            answer[i][j] = arr[i][j] 
    return answer
    
#     for i in range(col):
#         answer.append(arr[i])
        
#     if row==col:
#         return arr
    
#     if n==row:
#         for _ in range(row - col):
#             answer.append([0]*row)
            
#     elif n==col:
#         for i in range(col):
#             answer[i].append(0)

#     return answer