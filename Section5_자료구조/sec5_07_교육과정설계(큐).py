import sys
from collections import deque
sys.stdin=open("input_7.txt","rt")

pre=list(input())
n=int(input())
cnt=1

for _ in range(n) :
    cls=list(input())
    dq = deque(pre)

    for x in cls :
        if x in dq  :
            now=dq.popleft()
            if now==x :
                continue
            else :
                break

    if not dq :
        print("#"+str(cnt)+" YES")
    else :
        print("#"+str(cnt)+" NO")

    cnt+=1


