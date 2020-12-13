import sys

sys.stdin=open("input_10.txt","rt")
#이미 정렬된 상태임.
n= int(input())


re_arr= list(map(int, input().split()))

origin=[0]*n


for i in range(n) :
    for j in range(n) :
        if re_arr[i]==0 and origin[j]==0 :
            origin[j]=i+1
            break
        elif origin[j]==0 :
            re_arr[i]-=1

for i in origin :
    print(i, end=" ")
