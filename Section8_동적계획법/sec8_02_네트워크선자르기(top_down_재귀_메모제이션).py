import sys
sys.stdin=open("input_01.txt","rt")

def dfs(l) :
    if dy[l]!=0: # 가지커트 (메모제이션 하기 때문에 동적인것임)
        return dy[l]
    if l==1 or l==2 : # 이때가 종착점임
        return l
    else :
        dy[l]=dfs(l-2) +dfs(l-1)
        return dy[l]

if __name__=="__main__" :

    n=int(input())
    dy=[0]*(n+1)

    print(dfs(n))





