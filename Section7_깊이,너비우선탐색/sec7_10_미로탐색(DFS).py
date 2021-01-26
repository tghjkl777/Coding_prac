import sys
sys.stdin=open("input_10.txt","rt")

def dfs(l,point) :
    global cnt
    if point==[6,6] :
        cnt+=1
        return
    else :
        for i in range(4) :
            x=point[0]+dx[i]
            y=point[1]+dy[i]

            if 0<=x<=6 and 0<=y<=6 and maze[x][y]==0 :
                maze[point[0]][point[1]]=2
                dfs(l+1, [x,y])
                maze[point[0]][point[1]] = 0



if __name__=="__main__" :
    maze=[list(map(int, input().split())) for _ in range(7)]

    dx=[-1,0,1,0]
    dy=[0,1,0,-1]

    cnt=0

    dfs(0, [0,0])
    print(cnt)