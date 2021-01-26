#DFS로 풀기
import sys
sys.stdin=open("input_12.txt")

def dfs(x,y) :
    global cnt
    cnt+=1
    board[x][y]=0
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and board[xx][yy]==1 :
            dfs(xx,yy)


if __name__=="__main__":

    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    x=-1
    y=-1

    res = []
    cnt=0

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt=0
                dfs(i,j)
                res.append(cnt)

    res.sort()
    print(len(res))
    for x in res :
        print(x)



