import sys

sys.stdin=open("input_9.txt","rt")
#
# str1=list(input())
# str2=list(input())
#
# str1.sort()
# str2.sort()
#
# if str1==str2 :
#     print("YES")
# else :
#     print("NO")

#딕셔너리로풀기
str1=input()
str2=input()

dict1=dict()
dict2=dict()

for x in str1 :
    dict1[x]=dict1.get(x,0)+1 #키값에 해당하는 val값이 있으면 그것을 리턴 아니면 디폴트 값 리턴.
for x in str2 :
    dict2[x]=dict2.get(x,0)+1

if dict1.items()== dict2.items() :
    print("YES")
else :
    print("NO")

for i in dict1.keys() :
    if i in dict2.keys():
        if dict1[i]!=dict2[i]:
            print("NO")
            break
    else :
        print("NO")
        break
else :
    print("YES")
