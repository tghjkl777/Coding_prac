import sys

sys.stdin=open("input_6.txt","rt")

n=int(input())

people = [list(map(int, input().split())) for _ in range (n)]

# people.sort()
# #print(people)
#
# cnt=0
#
# for i in range(n) :
#     flag=0
#
#     for j in range(i+1, n ):
#         h= people[i][0]
#         w=people[i][1]
#        # print("now : ",h,w)
#
#         if h < people[j][0] and w < people[j][1]  :
#             flag=-1
#             break
#
#     if flag!=-1 :
#       #  print(h, w)
#         cnt+=1
#
# print(cnt)


# 키순으로 정렬한다음에 , 지금의 내가 제일 몸무게가 많이 나가야 한다.

people.sort(reverse=True)
print(people)

largest=0 # 몸무게 제일 큰거
cnt=0
for h, w in people :
    if w > largest :
        largest=w
        cnt+=1

print(cnt)