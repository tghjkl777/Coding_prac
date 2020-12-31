import sys
sys.stdin=open("input_11.txt","rt")

def dfs(l,s) :
    global  cnt
    if l==k :
        if sum(res)%m==0 :
            cnt+=1
    else :
        for i in range(s,n) :
            res[l]=arr[i]
            dfs(l+1,i+1)

if __name__=="__main__" :
    n,k=map(int, input().split())
    arr=list(map(int,input().split()))
    m=int(input())

    res=[0]*k
    cnt=0

    dfs(0,0)
    print(cnt)
