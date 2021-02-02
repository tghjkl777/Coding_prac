import sys
sys.stdin=open("input_13.txt","rt")

n=int(input())

dis=[[5000]*(n+1) for _ in range (n+1)] #큰수로 초기화

for i in range(1, n+1) :
    dis[i][i]=0

while(True) :
    p,q =map(int, input().split())
    if p==-1 and p==-1 :
        break
    else :
        dis[p][q]=1
        dis[q][p]=1

for k in range(1, n+1) :
    for i in range(1, n+1):
        for j in range(1,n+1) :
                dis[i][j]=min(dis[i][k]+dis[k][j],dis[i][j])
                dis[j][i]=dis[i][j]

res=[0]*(n+1)
for i in range(1,n+1) :
    res[i]=max(dis[i][1:])

ans=min(res[1:])
print(ans, res.count(ans))

for i in range(1,n+1) :
    if res[i]==ans :
        print(i, end=" ")


