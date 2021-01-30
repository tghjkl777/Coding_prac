import sys
sys.stdin=open("input_03.txt","rt")


def dfs(l) :
    if dy[l]!=0 :
        return dy[l]
    else :
        dy[l]=dfs(l-1)+dfs(l-2)
        return dy[l]


if __name__=="__main__" :
    n=int(input())

    dy=[0]*(n+1)
    dy[1]=1
    dy[2]=2

    print(dfs(n))