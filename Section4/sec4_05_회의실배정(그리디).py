import sys

sys.stdin=open("input_5.txt","rt")

n=int(input())

meeting=[list(map(int, input().split())) for _ in range(n)]

#회의가 끝나는 시간 기준으로 정렬이 필요하다.
meeting.sort(key=lambda x: x[1])

end=0
cnt=0

for s ,e in meeting :
   if s>= end : #시작하는 시간이 끝나는 시간보다 크거나 같을때
       end=e
       cnt+=1

print(cnt)