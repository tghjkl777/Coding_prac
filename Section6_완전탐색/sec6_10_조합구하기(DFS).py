import sys
sys.stdin=open("input_10.txt","rt")


def dfs(l) :
    global cnt,s
    if l==m :
        print(" ".join(map(str,res)))
        cnt+=1
        return
    else :
        for i in range(s,n+1) :
            s=i+1
            res[l]=i
            dfs(l+1)


if __name__=="__main__" :
    n,m=map(int, input().split())

    cnt=0
    res=[0]*m
    ch=[0]*(n+1)
    s=1


    dfs(0)
    print(cnt)


