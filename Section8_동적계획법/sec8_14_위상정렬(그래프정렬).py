import sys
from collections import deque
sys.stdin=open("input_14.txt","rt")

n,m =map(int, input().split())

work=[[0]*(n+1)for _ in range(n+1)]
res=[0]*(n+1) # 진입차수 계싼

for _ in range (m) :
    s,e= map(int, input().split())
    work[s][e]=1
    res[e]+=1

for x in work :
    print(x)
print()
print(res)

q=deque()
for i in range(1,n+1) :
    if res[i]==0 :
        q.append(i)
print(q)
ans=[]

while(q) :
    now = q.popleft()
    ans.append(now)
    for i in range(1, n+1) :
        if work[now][i]==1 :
            res[i]-=1
            if res[i]==0 :
                q.append(i)


print(ans)