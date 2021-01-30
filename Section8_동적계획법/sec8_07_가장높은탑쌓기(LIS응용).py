import sys
sys.stdin=open("input_07.txt","rt")

n=int(input())

a=[0]
h=[0]
w=[0]
arr=[]
max_h=[0]*(n+1)

for _ in range(n) :
    x,y,z=map(int, input().split())
    arr.append([x,y,z])

arr.sort(reverse=True)
arr.insert(0,[0,0,0])

#초기화화
max_h[1]=arr[1][1]

for i in range(2, n+1) :
    large=0
    for j in range(1,i) :
        if  arr[j][2] > arr[i][2] :
            if large < max_h[j] :
                large=max_h[j]
    max_h[i]=large+arr[i][1]

print(max(max_h))


