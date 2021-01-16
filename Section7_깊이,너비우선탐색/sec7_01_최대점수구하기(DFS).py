import sys
sys.stdin=open("input_01.txt","rt")

def dfs (l,sum, time) :
    global max_sum

    if l==n :
        if time > m :
            return
        else :
            if sum > max_sum :
                max_sum=sum

    else :
        dfs(l+1, sum+dic[l][0],time+dic[l][1])
        dfs(l + 1, sum , time )


if __name__ =="__main__" :

    n,m=map(int, input().split())

    dic=[]
    for _ in range(n) :
        s , t= map(int, input().split())
        dic.append([s,t])
    max_sum=-1
    dfs(0,0,0)
    print(max_sum)




