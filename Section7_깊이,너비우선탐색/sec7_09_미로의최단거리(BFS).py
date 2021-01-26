import sys
from collections import deque

sys.stdin=open("input_09.txt","rt")

miro=[list(map(int, input().split()))for _ in range(7)]
dis=[[0]*7 for _ in range(7)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

dq=deque()
dq.append((0,0))
miro[0][0]=1

while dq :
    now = dq.popleft()
    for i in range(4) :
        x=now[0]+dx[i]
        y=now[1]+dy[i]
        if 0<=x<=6 and 0<=y<=6 and miro[x][y]==0 :
            dq.append([x,y])
            miro[now[0]][now[1]] =1
            dis[x][y]=dis[now[0]][now[1]]+1


if dis[6][6]==0 :
    print(-1)
else :
    print(dis[6][6])
