import sys

sys.stdin=open("input_1.txt","rt")
n=int(input())

def binary(x) :
    if x==0 :
        return # 함수를 종료 시킴
    binary(x//2)
    print(x%2,end="")

binary(n)