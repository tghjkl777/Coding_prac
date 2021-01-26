import sys
from collections import deque
sys.stdin=open("input_07.txt","rt")


s,e=map(int, input().split())
ch=[0]*(10000+1)
load=[0]*(10000+1)

ch[s]=1
load[s]=0

dq=deque()
dq.append(s)

while(dq) :
    now=dq.popleft()
    if now ==e :
        print(load[now])
        break

    for next in (now-1,now+1,now+5) :
        if next >0 and next <=10000 :
            if ch[next]==0 :
                ch[next]=1
                dq.append(next)
                load[next]=load[now]+1






