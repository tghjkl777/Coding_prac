import sys
sys.stdin=open("input_1.txt","rt")

N, K= map(int,input().split())

list=[]
for i in range(1,N+1):
    if N%i==0:
        list.append(i)

if K > len(list) :
    print(-1)
else :
    print(list[K-1])

