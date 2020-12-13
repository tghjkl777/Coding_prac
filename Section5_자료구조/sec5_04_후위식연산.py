import sys

sys.stdin=open("input_4.txt","rt")

sik=input()
stk=[]
answer=0

for x in sik :
    if x.isdecimal():
        stk.append(x)

    else :
        b= int(stk.pop())
        a=int(stk.pop())
        if x=='+':
            answer=a+b
            stk.append(answer)
        elif x=='-' :
            answer=a-b
            stk.append(answer)

        elif x=='*' :
            answer=a*b
            stk.append(answer)
        elif x=='/' :
            answer=a/b
            stk.append(answer)

answer=stk.pop()

print(answer)





