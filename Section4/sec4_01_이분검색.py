import sys

sys.stdin=open("input_1.txt","rt")

N , M= map(int, input().split())
arr=list(map(int, input().split()))

arr.sort()

print(arr.index(M)+1)

#이분 검색 사용하기 , 정렬되어 있는 상황이 가정됨. 시간 복잡도 log(n)만에 가능하다.

start= 0
end= len(arr)-1
mid= end//2

while(True) :
    if M == arr[mid] :
        res= mid
        break
    elif M < arr[mid] :
        end= mid-1 # mid 는 이미 앞에서 검사 했으니까.
        mid = (start+end)//2
    else :
        start= mid+1
        mid = (start+end)//2



print(res+1)


