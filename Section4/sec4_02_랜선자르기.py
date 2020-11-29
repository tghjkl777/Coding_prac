import sys

sys.stdin=open("input_2.txt","rt")

k , n = map(int,input().split())

lan=[]

for _ in range(k) :
    lan.append(int(input()))

total =sum(lan)
res= total//n #다 합쳤을때 만들수 있는 최대 길이.

l=0
r=res
mid=(l+r)//2

while(l<=r) : # 이부분이 중요함

    count =0
    for i in lan :
        count+=i//mid

    if count < n :
        r=mid-1
        mid=(l+r)//2

    elif count >= n :
        l=mid+1
        mid = (l + r) // 2


print(mid)
