# 두 리스트 합치기
# 내 코드 : sort()함수가 nlogn의 시간 복잡도를 가지기 때문에 비효울적이다.#
'''
import sys
sys.stdin=open("input_4.txt",'rt')

arr=[]
for i in range(1,5) :
    if i%2==0 :
        arr=arr+list(map(int,input().strip().split()))
        arr.sort()

    else :
        input()
        continue

for a in arr :
    print(a,end=" ")
'''

# 예시 코드 : n의 시작복잡도를 가질수 있음. 이미 두 리스트가 정렬이 되어 있기 때문에

import sys
sys.stdin=open("input_4.txt",'rt')

N=int(input())
a=list(map(int,input().split()))
M=int(input())
b=list(map(int,input().split()))

p1=0
p2=0
c=[]

while p1<N and p2<M :
    if a[p1]<=b[p2]:
        c.append(a[p1])
        p1+=1
    else :
        c.append(b[p2])
        p2+=1

if p1 <N :
    c=c+a[p1:]
if p2< M :
    c=c+b[p2:]


for i in c :
    print(i, end=' ')

