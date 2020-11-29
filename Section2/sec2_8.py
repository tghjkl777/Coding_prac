#뒤집은 소수
import sys

sys.stdin=open("input_8.txt","rt")
n=int(sys.stdin.readline())
arr=sys.stdin.readline().split()

def num_reverse(x):
    reversed_num=x[::-1]
    reversed_num=int(reversed_num)

    return  reversed_num

""" int에서 뒤집는 방법
def reverse(x):
    res=0
    while(x>0):
        t=x%10 #나머지 값
        res=res*10+t
        x=x//10
    return res
"""

def isPrime(x): ##소수는 본수의 절만 까지 나눠 보면된다.
    if x == 1:
        return False
    for i in range(2,x//2+1) : # 절반 까지 포함 해야되니까 +1해준다
        if x%i==0 :
            return False
    else :
        return True



'''  div=2
    while(True):
        if x%div==0 :
            if x==div :
                return True
            return False
        else :
            div+=1'''

for i in arr :
    one_num=num_reverse(i)
    if isPrime(one_num)==True :
        print(one_num,end=" ")

