#대표값

import sys
sys.stdin=open("input_4.txt","rt")

N=int(sys.stdin.readline())
score=list(map(int,sys.stdin.readline().split()))

avg=sum(score)/len(score)
avg=round(avg)

dif=[]
for i in score :
    diff=abs(avg-i)
    dif.append(diff)
    mini=min(dif)
if dif.count(min(dif))==0 :
    print(avg,dif.index(min(dif)+1))
else :
    high_score=[]
    a=-1
    for i in range(dif.count(mini)):
        if a==-1:
            a=dif.index(mini)
            high_score.append(a)

        else :
            a=dif.index(mini,a+1)
            high_score.append(a)

    high=-1
    for j in range(len(high_score)) :
         if high < score[high_score[j]] :
            high=score[high_score[j]]
         elif high == score[high_score[j]] :
            pass
         else :
            pass

    print(avg,score.index(high)+1)


''' 모범 답안 
import sys
sys.stdin=open("input_4.txt","rt")

N=int(sys.stdin.readline())
score=list(map(int,sys.stdin.readline().split()))

avg=sum(score)/N
avg=round(avg) 

min=float("inf")
for i, one_score in enumerate(score) : # 리스트의 index 값과 실제갑 대응해줌
    tmp=abs(one_score-avg) #차이 계산
    if tmp<min :
        min=tmp
        pick_score=one_score # 답이되는 점수
        res=i+1 #답이되는 점수의 학생번호
    elif tmp==min : #차이가 같을때 점수가 높은 애가 답,
        if one_score >pick_score : #현재 점수가 그전의 점수보다 큼 , 점수가 같은면 학생번호가 작은애( 따로 안쓰고 지나가면됨.)
            score=one_score
            res=i+1

print(avg,res)

'''
