import sys
sys.stdin=open("input_12.txt","rt")

n,m=map(int, input().split())

dis=[[5000] *(n+1) for _ in range(n+1)] # 최대값으로 초기화

#초기화 과정
for i in range(1,n+1) :
    dis[i][i]=0
for _ in range(m) :
    s,e,d=map(int, input().split())
    dis[s][e]=d

# 값 구하기 *****
for k in range(1,n+1) :
    for i in range(1,n+1) :
        for j in range(1, n+1) :
            dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])

# 출력하기
for i in range(1,n+1) :
    for j in range(1,n+1) :
        if dis[i][j]==5000:
            print("M", end=" ")
        else :
            print(dis[i][j],end=" ")
    print()



