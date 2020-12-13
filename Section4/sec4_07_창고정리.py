import sys

sys.stdin=open("input_7.txt","rt")

l= int(input())
l_list=list(map(int, input().split()))
m=int(input())

l_list.sort()
# print(l_list)

distance=0
s=0
e=l-1

for _ in range(m) :
    l_list[s] += 1
    l_list[e] -= 1
    l_list.sort()
    # print(l_list)
    # if l_list[s] < l_list[s+1] :
    #     if l_list[e] > l_list[e-1] :
    #         pass
    #         # l_list[s]+=1
    #         # l_list[e]-=1
    #     else :
    #         e=e-1
    #
    # else :
    #     s=s+1
    #
    # l_list[s] += 1
    # l_list[e] -= 1

#print(l_list)
distance=l_list[l-1]-l_list[0]
print(distance)