import sys
sys.stdin=open("input_8.txt","rt")
def dfs(l):
    global  cnt
    if l==m :
        print(" ".join(map(str,res)))
        cnt+=1
        return
    else :
        for i in range(1,n+1) :
            if  i not in res[:l] :
                res[l]=i
            else :
                continue
            dfs(l+1)


if __name__=="__main__" :
    n, m= map(int, input().split())

    res=[0]*m
    cnt=0
    dfs(0)
    print(cnt)
