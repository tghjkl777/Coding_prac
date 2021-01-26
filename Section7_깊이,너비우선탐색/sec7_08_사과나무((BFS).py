import sys
sys.stdin=open("input_08.txt","rt")
from collections import deque
n=int(input())

dx=[-1,0,1,0]
dy=[0,1,0,-1]
apple=[]
for _ in range(n) :
    arr=list(map(int, input().split()))
    apple.append(arr)

c=n//2
dq=deque()
dq.append([c,c])
total=apple[c][c]
apple[c][c]=-1
l=0

while True :
    if l==c :
        break
    size=len(dq)
    for _ in range(size) :
        now= dq.popleft()

        for j in range(4) :
            x=now[0]+dx[j]
            y=now[1]+dy[j]
            if apple[x][y]!=-1 :
                total+=apple[x][y]
                apple[x][y]=-1
                dq.append([x,y])
    # for i in apple :
    #     print(i)
    l+=1

print(total)