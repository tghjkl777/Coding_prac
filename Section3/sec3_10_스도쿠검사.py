import sys

sys.stdin=open("input_10.txt","rt")

arr=[list(map(int, input().split())) for _ in range(9)]


dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]

for i in range(1,9,3):
    for j in range(1,9,3) :
        if all(arr[i][j] != arr[i+dx[k]][j+dy[k]] for k in range(8)) :
            answer="YES"
        else :
            answer="NO"
            break



if answer=="YES" :
    for a in arr :
        b=set(a)
        if len(b)!= 9 :
            answer="NO"
            #print(answer)
            break
    if answer =="YES" :
        for i in range(9) :
            c = set()
            for j in range(9):
                c.add(arr[j][i])

            if len(c)!=9 :
                answer = "NO"
                break


print(answer)