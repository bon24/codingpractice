def solution(n):
    answer = []
    a = [[0] * n for _ in range(n)]
    for v in range(n):
        a[0][v] = v+1
    i=n
    to_y=n-1
    to_x=n-1
    r , c =0 ,n-1
    while i < n**2:
        for _ in range(to_y): #아래
            r+=1
            i+=1
            a[r][c] = i
        print(r)
        to_y-=1
        for _ in range(to_x): #왼쪽
            i+=1
            c-=1
            a[r][c] = i
        to_x-=1
        print(c)
        for _ in range(to_y): #위
            i+=1
            r-=1
            a[r][c] = i
        to_y-=1
        print(r)
        for _ in range(to_x): #오른쪽
            i+=1
            c+=1
            a[r][c] = i
        print(c)
        to_x-=1        
#     위 아래 왼쪽 오른쪽 
    return a
# 좆같네 하기실ㅎ다
# 열을 끝까지 옮긴 후 마지막 열에서 행만 옮김 그리고 또 열 옮기고 이런식인데 그곳이 만약에 숫자로 채워져있으면 행에서 열로 또는 열에서 행으로 