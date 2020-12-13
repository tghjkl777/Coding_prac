import sys

sys.stdin=open("input_3.txt","rt")
sik=list(input())
stk=[]
answer=""

for x in sik :

    if x>='0' and x<='9' :
        answer+=x
    elif x==')' :
        while(stk) :
            if stk[-1]=='(' :
                stk.pop()
                break
            else :
                answer+=stk.pop()
    else :
        if not stk :
            stk.append(x)
        else :
            if x=='(':
                stk.append(x)

            elif x== '*' or x=='/' :
                while(stk) :
                    if stk[-1]=='*' or stk[-1]=='/':
                        answer+=stk.pop()
                    else :
                        break
                stk.append(x)

            elif  x=='+' or x=='-' :
                while(stk) :
                    if stk[-1] =='(' :
                        break
                    else :
                        answer+=stk.pop()
                stk.append(x)


while(stk) :
    answer+=stk.pop()

print(answer)

