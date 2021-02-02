import sys
sys.stdin=open("input_11.txt","rt")

n,m=map(int, input().split())

dy=[0]*(m+1)  # 시간으로 리스트 만든다. 내용은 점수

for _ in range(n) :
    s ,t =map(int, input().split())
    for i in range(m,t-1,-1) : #뒤에서 부터 읽는다. 
        dy[i]=max(dy[i],dy[i-t]+s)

print(dy[m])






