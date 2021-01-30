import sys
sys.stdin=open("input_05.txt","rt")

n=int(input())
arr=list(map(int, input().split()))
arr.insert(0,0)

dy=[0]*(n+1)
dy[1]=1
if arr[2]> arr[1] :
    dy[2]=2
else :
    dy[2]=1

for i in range(3, n+1):
    tmp=-1
    index=-1
    for j in range(1,i) :
        if arr[i] > arr[j] :
            if tmp < dy[j] :
                tmp=dy[j]
                index=j

    dy[i]=dy[index]+1

print(max(dy))

