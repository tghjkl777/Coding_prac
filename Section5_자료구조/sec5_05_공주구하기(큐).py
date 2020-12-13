import sys
from collections import deque
sys.stdin=open("input_5.txt","rt")

n , k = map(int,input().split())

queue=deque(i for i in range(1, n+1))

num=1
while(len(queue)!=1) :
    if (num==k) :
        queue.popleft()
        num=1
    else :
        a=queue.popleft()
        queue.append(a)
        num+=1

ans=queue.popleft()
print(ans)
