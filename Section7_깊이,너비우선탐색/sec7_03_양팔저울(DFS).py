import sys
sys.stdin=open("input_03.txt","rt")

def dfs(l,s_left, s_right) :
    if l==k :
        if s_left<s_right :
            weight=s_right-s_left
            total.add(weight)
    else :
        dfs(l+1,s_left+w[l], s_right)
        dfs(l+1, s_left, s_right+w[l])
        dfs(l+1,s_left,s_right)

if __name__=="__main__" :
    k=int(input())
    w=list(map(int,input().split()))

    s=sum(w)

    total=set()
    # for i in range(1, s+1) :
    #     total.append(i)

    dfs(0,0,0)
    print(s-len(total))
