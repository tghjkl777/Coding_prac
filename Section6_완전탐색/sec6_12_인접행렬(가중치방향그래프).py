import sys
sys.stdin=open("input_12.txt","rt")

n,m=map(int, input().split())
arr=[[0]*n for _ in range(n)]


for i in range(1,m+1) :
    s,e,w=map(int,input().split())
    arr[s-1][e-1]=w

for x in arr :
    for y in x :
        print(y,end=" ")
    print()