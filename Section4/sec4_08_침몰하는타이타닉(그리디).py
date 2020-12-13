import sys

sys.stdin=open("input_8.txt","rt")

n,m= map(int ,input().split())

weight = list(map(int, input().split()))


weight.sort()


cnt=0
s=0
e=n-1

while(s<=e) :
    if weight[s]+weight[e]<= m :
        cnt+=1
        s+=1
        e-=1
    else :
        cnt+=1
        e-=1


print(cnt)