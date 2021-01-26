#BFS로 풀기
import sys
from collections import deque
sys.stdin=open("input_12.txt")

n=int(input())
board= [list(map(int, input())) for _ in range(n)]

dq=deque()
dx=[-1,0,1,0]
dy=[0,1,0,-1]

res=[]

for i in range(n) :
    for j in range(n) :
        if board[i][j]==1 :
            dq.append((i,j))
            cnt=1
            board[i][j] = 0
            while dq :
                now= dq.popleft()
                for a in range(4) :
                    x=now[0]+dx[a]
                    y=now[1]+dy[a]

                    if 0<=x<n and 0<=y<n and board[x][y]==1 :
                        dq.append((x,y))
                        board[x][y] = 0
                        cnt+=1

            res.append(cnt)

print(len(res))
res.sort()
for x in res :
    print(x)