import sys
import itertools as it
sys.stdin=open("input_11.txt","rt")

if __name__=="__main__" :
    n,k=map(int, input().split())
    arr=list(map(int,input().split()))
    m=int(input())

    cnt=0
    for x in it.combinations(arr,k) :
        if sum(x)%m==0 :
            cnt+=1

    print(cnt)


