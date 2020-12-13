import sys

sys.stdin=open("input_8.txt","rt")

n=int(input())

# reserve=list(input() for _ in range(n) )
# use= list(input() for _ in range(n-1))
#
# reserve.sort()
# use.sort()
#
# i=0
# for x in use :
#     if x!= reserve[i] :
#         print(reserve[i])
#         break
#     i+=1


##################딕셔너리 사용하기

reserve=dict()

for _ in range(n) :
    now=input()
    reserve[now]=1

for _ in range(n-1) :
    now=input()
    reserve[now]=0

for key,val in reserve.items() :
    if val==1 :
        print(key)
