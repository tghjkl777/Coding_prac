import sys
sys.stdin=open("input_2.txt","rt")

test_num=int(sys.stdin.readline())

for i in range(1,test_num+1):
    n,s,e,k=map(int,sys.stdin.readline().split())

    #읽은 문자리스트를 인트형으로 바꾸는 방법
    big_list=list(map(int,sys.stdin.readline().split()))

    small_list=big_list[s-1:e]
    small_list.sort()

    print("#{}".format(i), end=" ")
    print("{}".format(small_list[k-1]))









