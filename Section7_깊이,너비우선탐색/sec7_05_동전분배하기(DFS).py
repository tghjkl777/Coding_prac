import sys
sys.stdin=open("input_05.txt","rt")

def dfs(l,a_sum,b_sum,c_sum) :
    global small
    if l==n :
        if a_sum==b_sum or b_sum ==c_sum or a_sum==c_sum :
            return
        else:
            if small > max(a_sum,b_sum,c_sum)-min(a_sum,b_sum,c_sum) :
                small=max(a_sum,b_sum,c_sum)-min(a_sum,b_sum,c_sum)


    else :
        sub=s-(a_sum+b_sum+c_sum)
        if (a_sum+sub) < b_sum or (a_sum+sub) <c_sum :
            return
        else :
            dfs(l+1,a_sum+coin[l],b_sum,c_sum)
            dfs(l+1,a_sum,b_sum+coin[l],c_sum)
            dfs(l+1,a_sum,b_sum,c_sum+coin[l])


if __name__=="__main__" :
    n=int(input())
    coin=[]
    for _ in range(n) :
        coin.append(int(input()))
    s=sum(coin)
    small=217000000
    dfs(0,0,0,0)
    print(small)