import sys
sys.stdin=open("input_10.txt","rt")

n=int(input())
coin=list(map(int, input().split()))
m=int(input())

dy=[1000]*(m+1)
dy[0]=0 # 0원을 거스러주는데 0개임. 이렇게 해놔야한다.

for x in coin :
    for i in range(x,m+1) :
            dy[i]=min(dy[i],dy[i-x]+1)

print(dy[m])