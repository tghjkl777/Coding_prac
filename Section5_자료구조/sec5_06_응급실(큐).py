import sys
from collections import deque
sys.stdin=open("input_6.txt","rt")

n,m = map(int, input().split())
patients=list(map(int, input().split()))

dq= deque((idx, val) for idx, val in enumerate(patients)) # 중요!!!!!
cnt=0

while(dq) :
    now=dq.popleft()
    if any(now[1] < x[1] for x in dq) :
        dq.append(now)
    else :
        cnt+=1
        if now[0]==m :
            break

print(cnt)
