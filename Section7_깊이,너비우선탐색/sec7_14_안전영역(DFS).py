import sys
sys.stdin=open("input_14.txt","rt")

sys.setrecursionlimit(10**6)
def dfs(x,y,h) :

    ch[x][y] = 1

    for i in range(4) :
        xx=x+dx[i]
        yy=y+dy[i]

        if 0<=xx<n and 0<=yy<n  and board[xx][yy] > h and ch[xx][yy]==0:
            dfs(xx,yy,h)


if __name__=="__main__" :
    n=int(input())
    board=[list(map(int, input().split())) for _ in range (n)]

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]


    res=[]
    for a in range(100) :
        h=a
        cnt=0
        ch = [[0] * n for _ in range(n)]
        for x in range(n) :
            for y in range(n) :
                if board[x][y] >h and ch[x][y]==0 :

                    dfs(x,y,h)
                    cnt+=1

        res.append(cnt)
        if cnt==0  :
            break
    print(max(res))