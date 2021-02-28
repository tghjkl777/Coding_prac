import turtle as t #그래픽 그려주기
import random as r
import time

class Brick() :
    def __init__(self):
        #벽돌 위치 초기화 맨위 가운데 지점
        self.x=6
        self.y=0
        self.color=r.randint(1,6)

    #키보드 움직임
    def move_left(self,grid):
        if grid[self.y][self.x-1]==0 and grid[self.y+1][self.x-1]==0 : # 대각선으로 가면 사라지는거 방지
            grid[self.y][self.x]=0
            self.x-=1

    def move_right(self,grid):
        if grid[self.y][self.x + 1] == 0 and grid[self.y+1][self.x+1]==0:
            grid[self.y][self.x] = 0
            self.x += 1

def draw_grid(block, grid) :
    block.clear()
    top=250
    left=-150

    color=["black","red","yellow","green","blue","purple","orange","white"]
    for i in range(len(grid)) :
        for j in range(len(grid[0])) :
            y=top-i*22
            x=left+j*22
            block.goto(x,y)

            #종료 지점 색깔 표시
            if i==15 and grid[i][j]==7 :
                block.color("red")
            else :
                block.color(color[grid[i][j]])

            block.stamp() # 그림 내용 도장찍기 (저장하기)

dy=[-1,0,1,0]
dx=[0,1,0,-1]
def DFS(y,x,grid,color) :
    global ch ,blank
    ch[y][x]=1
    blank.append((y, x))
    for i in range(4) :
        yy=y+dy[i]
        xx=x+dx[i]
        if 0<yy<24 and 0<xx<13:
            if ch[yy][xx]==0 and grid[yy][xx]==color :
                DFS(yy,xx,grid,color)

def max_height(grid) :
    for y in range(1,24) :
        for x in range(1, 13) :
            if grid[y][x]!=0 :
                return y

# 격자 업데이트 하기, 4개 이상 되면 없애기
def grid_update(grid, block) :
    for y,x in block :
        grid[y][x]=0

    height=max_height(grid) # 제일 높은 위치까지 for문 돌기
    #중력작용 구현
    for y in range(23,height,-1) :
        for x in range(1, 13) :
            if grid[y][x]==0 :
                tmp_y=y
                while(grid[tmp_y-1][x]==0 and tmp_y-1>0) :
                    tmp_y-=1
                grid[y][x]=grid[tmp_y-1][x]
                grid[tmp_y-1][x]=0

def continual_remove() :
    global  blank, ch
    while True :
        flag=1
        for y in range (23,15,-1) :
            for x in range(1,13) :
                if grid[y][x]!=0 :
                    ch = [[0] * 14 for _ in range(25)]
                    blank = []  # 같은 색깔 블록 행렬 튜플로 들어간다.
                    DFS(y, x, grid, grid[y][x])
                    if len(blank) >= 4:
                        grid_update(grid, blank)
                        flag=0

        draw_grid(block,grid)
        if flag==1 :
            break




def game_over() :
    pen.up()
    pen.goto(-120,100)
    pen.write("Game Over", font=("courier", 30))

#밑에 두줄까지 밖에 없을떄 이기는것임.
def you_win():
    pen.up()
    pen.goto(-100, 100)
    pen.write("You Win", font=("courier", 30))

if __name__=="__main__" :
    sc=t.Screen()
    sc.tracer(False) #  추적기능을 없애서 한방에 빠르게 그릴수 있다.
    sc.bgcolor("black")
    sc.setup(width=600,height=700)

    grid=[[0]*12 for _ in range(24)] # 안에 내용물 격자만들기

    #벽 격자 추가하기
    for i in range(len(grid)) :
        grid[i].insert(0,7)
        grid[i].append(7)
    grid.append([7]*14)

    #아래에서 3줄 설정하기 (기본 블럭)
    for i in range(23,20,-1) :
        for j in range(1,13) :
            grid[i][j]=r.randint(1,6)

    block=t.Turtle() # 그림 그려야 되니까 그리드 정보 담는 클래스 객체 만든다.
    block.penup()  # 그려지는 과정에서의 움직임 보여주는거 없앰.
    block.speed(0) # 0이 제일 빠르다.
    block.shape("square")
    block.setundobuffer(None) #안에 버퍼값 없애서 블럭 내려오는 속도 동일하게 만들어 준다.

    brick=Brick() # 벽돌 객체 생성
    grid[brick.y][brick.x]=brick.color # 객체에 대입한다.
    draw_grid(block, grid)

    #화면 글씨 출력
    pen=t.Turtle()
    pen.ht() #화살표 묘양 숨기기
    pen.goto(-80,290)
    pen.color("white")
    pen.write("Block Game", font=('courier',20))



    #키보드 입력 받기
    sc.onkeypress(lambda : brick.move_left(grid),"Left" )
    sc.onkeypress(lambda : brick.move_right(grid),"Right")
    sc.listen() # 프로그램 활성화 키 입력값 반영
    while(True) :
        sc.update() # 트래이스 없앴으면 updqte해주어여 한다.
        if grid[brick.y+1][brick.x]==0 :
            grid[brick.y][brick.x] = 0
            brick.y+=1
            grid[brick.y][brick.x] = brick.color
        else :

            #자기와 인접하고 색깔이 동일한 벽돌 개수 세기
            ch=[[0]*14 for _ in range(25)]
            blank=[] # 같은 색깔 블록 행렬 튜플로 들어간다.
            DFS(brick.y, brick.x,grid, brick.color)
            print(len(blank))

            #격자 업데이터 4개 이상 되면 없애고, 중력작용
            if len(blank)>=4:
                grid_update(grid,blank )
                continual_remove()

            height=max_height(grid)
            if height ==15 :
                game_over()
                break
            elif height>=22 :
                draw_grid(block,grid) #없어진거 한번 그려지고 유윈하는것임.
                you_win()
                break

            brick = Brick()  # 새로운 벽돌 생성

        draw_grid(block, grid)
        time.sleep(0.05) # while 문이 도는 시간을 조정해 준다. 게임의 속도를 조정해 줄수 있다.

    sc.mainloop() #이거 해야지 실행끝날때까지 안꺼진다.


