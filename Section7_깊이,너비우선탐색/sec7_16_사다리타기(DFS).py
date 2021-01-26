import sys
sys.stdin=open("input_16.txt","rt")

def dfs(x,y) :

    if x==0 :
        res=y
        print(res)
        sys.exit()
    else :
        for i in range(3) :
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<10 and 0<=yy<10 and board[xx][yy]==1 :
                board[xx][yy]=0
                dfs(xx,yy)

if __name__=="__main__" :
    board=[list(map(int, input().split())) for _ in range(10)]

    x=9
    y=0

    for i in range(len(board[9])) :
        if board[9][i]==2 :
            y=i
            break

    dx=[0,0,-1] #좌 오른 위
    dy=[-1,1,0]

    res=0
    board[x][y]=0
    dfs(x,y)
