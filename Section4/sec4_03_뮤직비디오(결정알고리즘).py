import sys

sys.stdin=open("input_3.txt","rt")

def count(capacity) :
    cnt=1
    # sum=0
    space=capacity
    for x in dvd:
        if x <= space :
            space=space-x
        else :
            space=capacity-x
            cnt+=1
    #     if sum+x>capacity:
    #         cnt+=1
    #         sum=x
    #     else:
    #         sum+=x

    return cnt

n , m= map(int,(input().split()))

dvd= list(map(int, input().split()))


rt=sum(dvd)
lt=1
answer=0

while(lt<=rt) :
    mid = (lt + rt) // 2
    if mid >= max(dvd) and count(mid) <= m :
        answer=mid
        rt=mid-1

    else :
        lt=mid+1


print(answer)

