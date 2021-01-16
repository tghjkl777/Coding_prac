import sys
sys.stdin=open("input_02.txt","rt")

def dfs(l,m_sum) :
    global  total
    if l==n+1 :
        if m_sum > total :
            total=m_sum
    else :
        if l+day[l]<=n+1 :
            dfs(l+day[l],m_sum+money[l])
        dfs(l+1, m_sum)

if __name__=="__main__" :
    n= int(input())

    day=[0]*(n+1)
    money=[0]*(n+1)
    for i in range(1,n+1) :
        d, m = map(int, input().split())
        day[i]=d
        money[i]=m

    total=-1
    dfs(1,0) #레벨,day, 돈합
    print(total)



