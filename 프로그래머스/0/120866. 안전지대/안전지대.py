# 폭탄위치는 1 안전지대가 아닌곳은 2로 안전지대인곳은 0으로
def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                    for x in range(-1,2):
                        if 0<=i+x<len(board):
                            if 0<=j<len(board) and board[i+x][j] != 1:
                                board[i+x][j] = 2
                            if 0<=j-1<len(board) and board[i+x][j-1] != 1:
                                board[i+x][j-1] = 2
                            if 0<=j+1<len(board) and board[i+x][j+1] != 1:
                                board[i+x][j+1] = 2
    print(board)
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                answer+=1
    return answer