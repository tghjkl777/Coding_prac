#소수(에라토스테네스 체)
import sys

sys.stdin=open("input_7.txt","rt")
n= int(sys.stdin.readline())

arr=[0]*(n+1)

#내가 짠거
for i in range(2,n+1):
    if arr[i]==0:
        for j in range(i*2,n+1,i) :
            arr[j]=1

print(arr.count(0)-2)

'''모범 답안
cnt=0 # 카운트를 줘서 하나씩 더하는걸로 함. 그래서 2도 arr에서 1로 체크된다.
for i in range(2,n+1):
    if arr[i]==0:
        cnt+=1
        for j in range(i,n+1,i) :
            arr[j]=1

print(cnt)

'''