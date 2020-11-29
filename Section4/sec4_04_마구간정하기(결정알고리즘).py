import sys

sys.stdin= open("input_4.txt","rt")

n,c = map(int, input().split())


space =[]

for _ in range(n):
    space.append(int(input()))

space.sort()

rt=1
lt=space[-1]


def count(short) :
    cnt=1
    now=space[0]
    for i in range(1, len(space)):
        if space[i]-now >= short :
                cnt+=1
                now=space[i]

    return cnt

answer=0
while rt <=lt :
    mid = (rt + lt) // 2
    if count(mid) < c :
        lt=mid-1
    else :
        answer=mid
        rt=mid+1


print(answer)