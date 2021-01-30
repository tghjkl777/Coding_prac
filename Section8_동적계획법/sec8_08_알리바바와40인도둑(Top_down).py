import sys
sys.stdin=open("input_08.txt","rt")

def dfs(ii,jj) :
    # if dy[ii][jj] !=0 :
    #     return dy[ii][jj]
    # else:
    #     dy[ii][jj]=arr[ii][jj]+min(dfs(ii-1,jj),dfs(ii,jj-1))
    #     return dy[ii][jj]

#모범 답안 시작---------------
    if dy[ii][jj] !=0 :
        return dy[ii][jj]
    if ii==0 and jj==0 : #종료지점
        return arr[0][0]
    else :
        if jj==0 :
            dy[ii][jj]=dfs(ii-1,jj) +arr[ii][jj]
        elif ii==0 :
            dy[ii][jj]=dfs(ii,jj-1)+arr[ii][jj]

        else :
            dy[ii][jj] = arr[ii][jj] + min(dfs(ii - 1, jj), dfs(ii, jj - 1))
        return dy[ii][jj]
#-------------------모범 답안 끝
if __name__=="__main__" :
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    dy = [[0] * n for _ in range(n)] #메모제이션

    #초기화
    # dy[0][0]=arr[0][0]
    # for i in range(1,n) :
    #         dy[0][i]=arr[0][i]+dy[0][i-1]
    #         dy[i][0]=arr[i][0]+dy[i-1][0]

    print(dfs(n-1,n-1))
