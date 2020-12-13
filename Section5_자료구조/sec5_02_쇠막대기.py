import sys

sys.stdin=open("input_2.txt","rt")

arr= list(input())

stk=[]
last=''

cnt=0

for i in arr :
    if not stk :
        stk.append(i)
    else :
        if i==')' and stk[-1]=='(' and last=='(' : #레이저
            stk.pop()
            cnt+=len(stk)
        elif i==')' and stk[-1]=='(' and last==')':
            stk.pop()
            cnt+=1
        else :
            stk.append(i)
    last=i

print(cnt)
