#회문 문자열 검사

import sys

sys.stdin=open("input_1.txt","rt")

n=int(sys.stdin.readline())

for i in range(n):
    string =str(sys.stdin.readline().splitlines())
    string=string.strip('[]\'')
    string=string.lower()
    if string==string[::-1] :
        print("#{} YES".format(i+1))
    else :
        print("#{} NO".format(i+1))