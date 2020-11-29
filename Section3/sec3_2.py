# 숫자만 추출
import sys
sys.stdin=open('input_2.txt','rt')

str=sys.stdin.readline()

num=[]
for a in str :
    if a.isdigit() :
        num.append(a)

num=''.join(num)
num=int(num)

cnt=0

for i in range(1,num+1) :
    if num%i==0 :
        cnt+=1

print(num)
print(cnt)

