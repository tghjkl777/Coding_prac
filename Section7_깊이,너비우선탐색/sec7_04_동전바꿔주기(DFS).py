import sys
sys.stdin=open("input_04.txt","rt")


def dfs(l,sum) :
    global cnt
    if sum==paper :
        cnt+=1
        return
    if sum >paper :
        return
    if l==total:
        return
    else :

        for i in range(coin_list[l][1],-1,-1) :
            dfs(l+1, sum+coin_list[l][0]*i)

if __name__=="__main__" :
    paper=int(input())
    total=int(input())
    coin_list=[]

    for _ in range(total) :
        a,b=map(int, input().split())
        coin_list.append([a,b])
    coin_list.sort(reverse=True)
    cnt=0

    dfs(0,0)
    print(cnt)