import sys

sys.stdin=open("input_8.txt","rt")

N=int(input())

gam=[ list(map(int,input().split())) for _ in range(N)]

M=int(input())

order=[list(map(int, input().split())) for _ in range(M)]

for a,b,c in order :

    if b==0 :
        for i in range(c) :
            gam[a-1].append(gam[a-1].pop(0))
        #gam[a-1]=gam[a-1][c:]+gam[a-1][:c]

    else :
        for i in range(c) :
            gam[a-1].insert(0,gam[a-1].pop())





total=0

s=0
e=N-1

for i in range(N):
    for j in range(s,e+1):
        total+=gam[i][j]


    if i>=N//2 :
        s-=1
        e+=1
    else :
        s+=1
        e-=1

print(total)
