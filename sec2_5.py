#정다면체

import sys
sys.stdin=open("input_5.txt","rt")

n,m= map(int,sys.stdin.readline().split())

sum=[]

for i in range(1,n+1) :
    for j in range(1,m+1):
        sum.append(i+j)

result=[]
cnt=[]
for i in range(len(sum)):
    result.append([sum[i],sum.count(sum[i])])
    cnt.append(sum.count(sum[i]))

high=max(cnt)
a=set()
for i, j in result :
    if j==high :
        a.add(i)

a=list(a)
b=" ".join(map(str,a))
print(b)



'''모범 답안

cnt=[0 for i in range(n+m+1)]

for i in range(1,n+1) :
    for j in range(1,m+1):
        cnt[i+j]+=1

high=max(cnt)
for i in range(len(cnt)) :
    if cnt[i]==high :
        print(i,end=" ")

'''