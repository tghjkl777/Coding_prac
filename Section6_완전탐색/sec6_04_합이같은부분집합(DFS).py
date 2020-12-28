import sys

sys.stdin=open("input_4.txt","rt")


def dfs(v) :
    global answer #  이 함수 안에서 전역변수로 사용하겠다는 선언임
    if answer=="YES" :
        return
    else:

        if v >= len(origin) :
            total=sum(origin)

            sum1=0
            for i in range(len(check)) :
                if check[i]==1 :
                    sum1+=origin[i]

            if total/2==sum1 :
                answer="YES"
            else :
                answer="NO"

        else :
            check[v]=1
            dfs(v+1)
            check[v]=0
            dfs(v+1)


if __name__=="__main__" : # main 이하 변수들은 다 전역변수이다.

    n=int(input())
    origin=list(map(int, input().split()))
    check=[0]*n

    answer=""

    dfs(0)
    print(answer)

