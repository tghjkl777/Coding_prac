import sys
sys.stdin=open("input_15.txt","rt")
from collections import deque

m,n =map(int, input().split())
board=[list(map(int, input().split())) for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]

dq=deque()

for a in range(n) :
    for b in range(m) :
        if board[a][b]==1:
            dq.append((a,b))

day=0
while(dq) :

    l=len(dq)
    for _ in range(l) :
        now=dq.popleft()
        for i in range(4) :
            x=now[0]+dx[i]
            y=now[1]+dy[i]

            if 0<=x<n and 0<=y<m and board[x][y]==0 :
                board[x][y]=1
                dq.append((x,y))

    if len(dq)==0 and day==0 :
        print(day)
        sys.exit()

    else :
        day+=1

        flag=False
        for a in range(n):
            for b in range(m):
                if board[a][b] == 0:
                    flag=True
                    break
            if flag==True :
                break
        if flag ==True :
            continue
        else :
            break


for a in range(n) :
    for b in range(m) :
        if board[a][b]==0 :
            day=-1

print(day)