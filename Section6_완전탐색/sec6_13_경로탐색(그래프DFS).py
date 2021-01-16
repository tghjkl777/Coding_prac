import sys
sys.stdin=open("input_13.txt","rt")


def dfs(v):
    global cnt
    if v==n :
        cnt+=1
    else:
        if ch[v]==0 :
            ch[v]=1
            for i in range(1,n+1) :
                if arr[v][i]==1 :
                    dfs(i)
            ch[v]=0

if __name__=="__main__" :
    n,m=map(int, input().split())
    arr=[[0]*(n+1) for _ in range(n+1)]

    for i in range(m) :
        s,e =map(int, input().split())
        arr[s][e]=1

    ch=[0]*(n+1)
    cnt=0
    dfs(1)
    print(cnt)


