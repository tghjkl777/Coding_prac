import sys

sys.stdin=open("input_7.txt","rt")

N=int(input())

apple=[list(map(int, input().split())) for _ in range(N)]

half=N//2

#가운데 한번
total=sum(apple[half])

for i in range(half) :
    for j in range(half-i,half+i+1) :
        total+=apple[i][j]


for i in range(half+1,N) :
    for j in range(i-half,half+(half-(i-half))+1) :
        total+=apple[i][j]

print(total)