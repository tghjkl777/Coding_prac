import sys
sys.stdin=open("input_06.txt","rt")

def dfs(l) :
    global cnt
    if l==len(crpto) :
        print("".join(answer))
        cnt+=1
    else:
        if crpto[l]!=0:
            one_char=chr(crpto[l]+64)
            answer.append(one_char)
            dfs(l+1)
            answer.pop()

        if(l+2<=len(crpto)) :
            num=int("".join(list(map(str,crpto[l:l+2]))))
            if num >=10 and num<=26:
                two_char=chr(num+64)
                answer.append(two_char)
                dfs(l+2)
                answer.pop()


if __name__=="__main__" :

    crpto=list(map(int, input()))
    cnt=0
    answer=[]
    dfs(0)
    print(cnt)