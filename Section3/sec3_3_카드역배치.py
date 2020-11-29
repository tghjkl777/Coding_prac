# 카드 역배치 : 나의 코드 : 시간 초과...
import sys
sys.stdin=open("input_3.txt","r")

card=list(range(0,21))

# while(True):
#     one_line =sys.stdin.readline().strip()
#
#     # Eof시 while 문 빠져 나가기.
#     if not one_line:
#         break
#
#     start, end= map(int, one_line.split())
#     card[start:end+1] = reversed(card[start:end+1])

for _ in range(10):
    start, end= map(int, input().split())
    for i in range((end-start+1)//2) :
        card[start+i], card[end-i] =card[end-i],card[start+i]

for i in card[1:] :
    print(i, end=' ')


## 예시코드
'''
import sys
sys.stdin=open("input.txt", "r")

a=list(range(21))

for _ in range(10): # 변수없이 10번 실행하는것.
    s, e=map(int, input().split())

    for i in range((e-s+1)//2): # 몇 덩어리로 나뉘어져 실행되는지.
        a[s+i], a[e-i]=a[e-i], a[s+i]  #첫 지점과 끝지점 서로 swap 하는것.

a.pop(0) # 0번째 숫자 빼는것임.

for x in a:
    print(x, end=' ')
'''