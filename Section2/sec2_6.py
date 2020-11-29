#자릿수의 합

import sys
sys.stdin=open("input_6.txt" ,"rt")

n=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split()))


def digit_sum(x):
    value=[]
    a=x
    while(True):
        value.append(a%10)
        a=a//10
        if a==0 :
            break

    return sum(value)

sum_list=[]
for i in range(len(num)) :
    sum_list.append(digit_sum(num[i]))

maximum=max(sum_list)
print(num[sum_list.index(maximum)])
'''
#모범 답안
def digit_sum(x):
    sum=0
    for i in str(x):
        sum+=int(i)

    return sum

maxx=-1
for x in num :
    total=digit_sum(x)
    if maxx < total :
        maxx=total
        res=x

print(res)

'''