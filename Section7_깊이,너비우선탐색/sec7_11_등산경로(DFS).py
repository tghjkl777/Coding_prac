import sys
sys.stdin=open("input_11.txt","rt")


def dfs(xx,yy) :
    global  cnt
    if xx==max_x and yy==max_y :
        cnt+=1
    else :
        for i in range(4) :
            x=xx+dx[i]
            y=yy+dy[i]

            if 0<=x<n and 0<=y<n :
                if mount[xx][yy] < mount[x][y] :
                    dfs(x,y)

if __name__=="__main__" :
    n=int(input())

    mount=[list(map(int, input().split())) for _ in range(n)]

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    max_x=0
    max_y=0

    min_x=0
    min_y=0

    big=-1
    small=2170000

    for i in range(n) :
        for j in range(n) :
            if mount[i][j] > big :
                max_x=i
                max_y=j
                big=mount[i][j]
            if mount[i][j] <small :
                min_x=i
                min_y=j
                small=mount[i][j]

    cnt=0

    dfs(min_x,min_y)
    print(cnt)





