import sys
sys.stdin=open("input_9.txt","rt")

def dfs(l,sum_p) :
    global p
    if l==n and sum_p==f :
        print(" ".join(map(str,p)))
        sys.exit(0) # 최초로 발견됬기 대문에 종료함.

    else :
        #순열 만들어 내기
        for i in range(1, n+1) :
            if ch[i]==0 :
                ch[i] = 1
                p[l]=i

                dfs(l+1,sum_p+p[l]*b[l])
                ch[i]=0  # 백에서 0으로


if __name__=="__main__" :
    n,f=map(int,input().split())
    print(n,f)

    p=[0]*n # 순열 값 초기화
    b=[1]*n # 곱셈 값 초기화 이항 개수 곱
    ch=[0]*(n+1) # 값 초기화 하는 것 체크용도

    for i in range(1,n) :
        b[i]=b[i-1]* (n-i)//i

    dfs(0,0)




