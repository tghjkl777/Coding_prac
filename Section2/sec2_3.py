#K번째 큰수
import sys

sys.stdin=open("input_3.txt","rt")

n,k = map(int, sys.stdin.readline().split())
card=list(map(int,sys.stdin.readline().split() ))

card.sort(reverse=True)
sum=[]
for i in range(n):
    for j in range(i+1,n):
        for l in range(j+1,n):
            sum.append(card[i]+card[j]+card[l])

#리스트 중복제거-> 리스트 변환
sum=list(set(sum))
sum.sort(reverse=True)
print(sum[k-1])

