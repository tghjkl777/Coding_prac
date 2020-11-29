#주사위 게임
import sys

sys.stdin=open("input_9.txt","rt")

n=int(sys.stdin.readline())

dice=[]
money=0
money_list=[]
for i in range(n):
    dice=list(map(int,sys.stdin.readline().split()))
    dice_set=set(dice)
    if len(dice_set)==3 :
        money=max(dice)*100
        money_list.append(money)
    elif len(dice_set)==2:
        if dice[0]==dice[1]:
            money=1000+dice[0]*100
        if dice[0]==dice[2]:
            money = 1000 + dice[0] * 100
        if dice[1]==dice[2]:
            money = 1000 + dice[1] * 100
        money_list.append(money)
    else :
        money=10000+dice[0]*1000
        money_list.append(money)


print(max(money_list))
'''
#모범답안

res=0
for i in range(n):
    tmp=sys.stdin.readline().split()
    tmp.sort()
    a,b,c=map(int,tmp)


    if a==b and b==c :
        money=10000+a*1000
    elif a==b or a==c :
        money=1000+a*100
    elif b==c :
        money = 1000 + b * 100
    else :
        money=c*100

    if res < money :
        res=money

print(res)

'''