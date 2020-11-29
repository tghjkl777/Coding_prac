#수들의 합 : 내꺼 time out 걸림....
import sys

sys.stdin=open("input_5.txt",'rt')

N,M= map(int, sys.stdin.readline().split())
arr=list(map(int, input().split()))

cnt=0

for i in range(1,M+1):
     j=0
     for j in range(len(arr)):
         total=sum(arr[j:j+i])
         if total== M and i+j<=N :
          cnt+=1

print(cnt)


#'''
#예시 풀이
import sys
sys.stdin=open("input_5.txt",'rt')

N,M= map(int, sys.stdin.readline().split())
arr=list(map(int, input().split()))

tot=0
lp=0
rp=1

while(True) :
    if tot < M :
        tot

#'''



