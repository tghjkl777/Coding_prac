import sys
import heapq as hq

sys.stdin=open("input_10.txt","rt")
a=[]

while(True) :
    now=int(input())
    if now==-1:
        break
    elif now==0 :
        if not a :
            print(-1)
        else :
            print(hq.heappop(a))
    else :
        hq.heappush(a,now)





