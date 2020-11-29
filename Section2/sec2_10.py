#점수 계산

import sys

sys.stdin=open("input_10.txt","rt")
n=int(sys.stdin.readline())

correct=list(map(int,sys.stdin.readline().split()))
score_sum=0
cnt=0

for i in range(len(correct)) :
    if i==0 and correct[i]==1 :
        score_sum=1
        cnt=1
    else :

        if correct[i]==1 and cnt!=0 :
            cnt+=1
            score_sum+=cnt
        elif correct[i]==1 and cnt==0 :
            cnt=1
            score_sum+=cnt
        else :
            cnt=0

print(score_sum)
'''
#모범 답안
for i in correct :
    if i==1 :
        cnt+=1
        score_sum+=cnt
    else :
        cnt=0

print(score_sum)
'''