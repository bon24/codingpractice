def solution(keyinput, board):
    answer = []
    
    x,y=0,0
    x_lim,y_lim = (board[0]-1)//2, (board[1]-1)//2
    
    dic = {"up":1,"down":-1,"right":1,"left":-1}
    
    for i in keyinput:
        if i=="up" or i=="down":
            if abs(y+dic[i])<=y_lim:
                y+=dic[i]
        else:
             if abs(x+dic[i])<=x_lim:   
                x+=dic[i]
    answer = [x,y]
            
    return answer