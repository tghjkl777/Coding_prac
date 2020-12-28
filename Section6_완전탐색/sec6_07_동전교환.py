import sys

def dfs(l,sum)  :
    global res
    if l> res : # 이전보다 길이기 길면 사전에 cut
        return
    if sum > money:
        return
    if  sum==money :
        if l<res :
            res=l
    else :
        for i in range(n) :
            dfs(l+1,sum+coin[i])


if __name__=="__main__" :
    sys.stdin=open("input_7.txt","rt")

    n=int(input())
    coin=list(map(int, input().split()))
    money=int(input())
    res=2147000000

    coin.sort(reverse=True) # 가지 뻗을때 빨리끝낼려고. 너무 깊이 가지 않을려고

    dfs(0,0)
    print(res)
