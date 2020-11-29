import sys

sys.stdin=open("input_11.txt","rt")

arr=[list(map(int, input().split())) for _ in range(7)]

answer=0

#슬라이싱을 잘하자. arr[4:-1:-1]이런식으로는 안된다.
for i in range(7) :
    for j in range(7) :

        #행만
        if j<=2 and i >2 :
            temp=arr[i][j:j+5]
            if temp==temp[::-1] :
                answer+=1


        #열만
        if j> 2 and i <=2 :
            if arr[i][j]==arr[i+4][j] and arr[i+1][j]==arr[i+3][j] :
                answer+=1


        #행열 같이
        if j<=2 and i<=2 :
            temp = arr[i][j:j + 5]
            if temp == temp[::-1]:
                answer+=1

            if arr[i][j]==arr[i+4][j] and arr[i+1][j]==arr[i+3][j] :
                answer+=1




print(answer)