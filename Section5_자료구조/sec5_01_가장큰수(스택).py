import sys

sys.stdin=open("input_1.txt","rt")

n , m =map(int, input().split())

arr=list(map(int, str(n)))

stk=[]

cnt=m

for i in arr :
    while stk and cnt>0 and stk[-1]< i :
        cnt-=1
        stk.pop()
    stk.append(i)

if cnt!=0 :
    stk=stk[:-cnt]

print("".join(map(str,stk)))
