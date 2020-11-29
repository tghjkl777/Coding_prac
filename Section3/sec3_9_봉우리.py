import sys

sys.stdin=open("input_9.txt","rt")

N=int(input())

arr = [list(map(int ,input().split())) for _ in range(N)]


for i in range(N) :
    arr[i].insert(0,0)
    arr[i].append(0)

zero=[]

for _ in range(N+2) :
    zero.append(0)

arr.insert(0,zero)  # arr.insert(0, [0]*n)
arr.append(zero)


answer=0

for i in range(1, N+1) :
    for j in range(1,N+1) :
        now= arr[i][j]
        up = arr[i-1][j]
        down = arr[i+1][j]
        left= arr[i][j-1]
        right= arr[i][j+1]
        if now > up and now >down and  now> left and now >right : # all()함수를 사용해보자!!!
            answer+=1


print(answer)