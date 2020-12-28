import sys

def dfs(l) :
    global  cnt

    if l>=m : #종료지점
        print(" ".join(map(str,res)))
        cnt+=1
        return
    else :
        for i in range(1,n+1) :
            res[l]=i
            dfs(l+1)

if __name__=="__main__" :
    sys.stdin = open("input_6.txt", "rt")
    n,m =map(int,input().split())

    cnt=0
    res=[0]*m
    dfs(0)

    print(cnt)



