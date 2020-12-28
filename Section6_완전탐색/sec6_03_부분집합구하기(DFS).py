import sys
sys.stdin=open("input_3.txt","rt")

def dfs(v) :

    if v==n+1: # 끝에 도달했을때 체크리스트 다 출력함.
        for i in range(1,n+1) :
            if check[i]==1 :
                print(i,end=" ")
        print()
    else :
        check[v]=1
        dfs(v+1)
        check[v]=0
        dfs(v+1)


if __name__=="__main__" :
    global n
    global  check
    n = int(input())
    check=[0]*(n+1)
    dfs(1)