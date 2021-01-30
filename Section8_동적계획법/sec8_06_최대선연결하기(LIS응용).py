import sys
sys.stdin=open("input_06.txt","rt")

n=int(input())
arr=list(map(int, input().split()))
arr.insert(0,-1)
dy=[0]*(n+1)

#최기화
dy[1]=1
for i in range(2, n+1) :
    large=0
    for j in range(1,i) :
        if arr[j] < arr[i] :
            if large <dy[j] :
                large=dy[j]
    dy[i]=large+1

print(max(dy))

