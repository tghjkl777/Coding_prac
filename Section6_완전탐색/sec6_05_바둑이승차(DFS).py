import sys
sys.stdin=open("input_5.txt")
# limit time 에러 났음.
def dfs(v,summ) :
    global answer

    if summ > c :
        return
    if  summ+sum(arr[v:]) < answer :
        return

    if v >= n: # 종료지점에 온것임.
        if summ > answer :
            answer=summ
    else :

        total=summ+arr[v]
        dfs(v+1,total)
        dfs(v+1,summ)

if __name__=="__main__" :
    c,n=map(int,input().split())

    arr=[]
    for i in range(n) :
        arr.append(int(input()))

    total=sum(arr)
    answer=0 #최종적인 답 저장.
    dfs(0,0)
    print(answer)


