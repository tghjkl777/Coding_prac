import sys
sys.stdin=open("input_09.txt","rt")

n,m = map(int, input().split())

w=[]
p=[]
dy=[0]*(m+1)

for i in range(n) : # 보석 수만큼 돌아서 하나씩 읽기
    w,p=map(int, input().split())

    for j in range(w,m+1) : # 음스를 제외하고 도는것
        if j-w >=0 :
            dy[j]=max(dy[j],dy[j-w]+p)

print(dy[m])

