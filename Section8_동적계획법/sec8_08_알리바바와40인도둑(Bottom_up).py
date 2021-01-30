import sys
sys.stdin=open("input_08.txt","rt")

n=int(input())

arr=[list(map(int, input().split())) for _ in range(n)]

dy=[[0]*n for _ in range(n)]
dy[0][0]=arr[0][0]

for i in range (n) :
    for j in range(n) :
        if dy[i][j]==0 :
            if 1<=i<n and 1<=j<n :
                dy[i][j]=arr[i][j]+min(dy[i-1][j],dy[i][j-1])
            else :
                #앞에서 미리 초기화 가능함
                if i==0 :
                    dy[i][j]=arr[i][j]+dy[i][j-1]
                elif j==0 :
                    dy[i][j] = arr[i][j] + dy[i-1][j]

print(dy[n-1][n-1])