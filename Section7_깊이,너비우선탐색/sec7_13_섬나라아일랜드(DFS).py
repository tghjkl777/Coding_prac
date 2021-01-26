import sys
sys.stdin=open("input_13.txt","rt")

def dfs(x,y) :
    board[x][y] = 0
    for ii in range(8) :
        xx=x+dx[ii]
        yy=y+dy[ii]

        if 0<=xx<n and 0<=yy<n and board[xx][yy]==1 :
            dfs(xx,yy)


if __name__=="__main__" :
    n=int(input())
    board=[list(map(int, input().split())) for _ in range (n)]

    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]

    cnt=0
    for i in range(n) :
        for j in range(n) :
            if board[i][j]==1 :
                dfs(i,j)
                cnt+=1

    print(cnt)