#타임 리밋 걸림 하
import sys
sys.stdin=open("input_6.txt",'rt')

N=int(input())

lines= sys.stdin.readlines()

arr1=[]

total=0
for line in lines :
    line=line.strip()
    arr=list(map(int, line.split()))
    arr1.append(arr)

    a=sum(arr)
    if( a> total) :
        total=a

for i in range(N):
    res = 0
    for j in range(N):
        res+=arr1[j][i]

    if(res> total) :
        total= res
res1=0
res2=0
for i in range(N):
    res1+=arr1[i][i]
    res2+=arr1[N-1-i][i]


total=max(res1,res2,total)

print(total)

#예시 답안

import sys
sys.stdin = open("input.txt", 'r')
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]  # 한줄에 읽어서 리스트화까지 시켜줌
largest=-2147000000
for i in range(n):
    sum1=sum2=0
    for j in range(n):
        sum1+=a[i][j]
        sum2+=a[j][i]
    if sum1>largest:
        largest=sum1
    if sum2>largest:
        largest=sum2
sum1=sum2=0
for i in range(n):
    sum1+=a[i][i]
    sum2+=a[i][n-i-1]
if sum1>largest:
    largest=sum1
if sum2>largest:
    largest=sum2
print(largest)






