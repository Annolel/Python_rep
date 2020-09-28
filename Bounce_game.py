from tkinter import *
import random
import time


class Ball:

    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        #определение доски чтоб шарик понимал что она есть
        self.paddle = paddle
        self.score = score
        #в self.id будет хранится индекс созданого кружка
        self.id=canvas.create_oval(10,10,25,25,fill=color)
        #теперь по этому индексу мы двигаем его в середину экрана
        self.canvas.move(self.id,245,100)
        #х - диагональ, у - вертикаль, изначально кружок движется вверх.
        starts=[-3,-2,-1,1,2,3]
        random.shuffle(starts)
        #кружок движется в рандомном направлении и рандомной скоростью по x
        self.x=starts[0]
        #но по у вверх
        self.y=-3
        #winfo_heingt возвращает высоту окна чтоб знать где потолок и пол
        self.canvas_height=self.canvas.winfo_height()
        #canvas_width определяет где стены
        self.canvas_width=self.canvas.winfo_width()
        #по умолчанию он не касается дна
        self.hit_bottom = False

    def hit_paddle(self,pos):
        paddle_pos=self.canvas.coords(self.paddle.id)
        if pos[2]>=paddle_pos[0] and pos[0]<=paddle_pos[2]:
            if pos[3]>=paddle_pos[1] and pos[3]<=paddle_pos[3]:
                self.score.hit()
                return True
            return False

    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        #возвращает координаты объекта self.id в переменную pos в виде 4 цифр:
        #х,у верхней левой точки и х,у нижней правой [255.0, 29.0, 270.0, 44.0]
        pos=self.canvas.coords(self.id)
        #проверяем не уперся ли верх кружка в потолок.
        if pos[1] <=0:
        #если уперся то двигаемся вниз
            self.y=3
        #проверяем не уперлся ли кружок в пол
        if pos[3] >= self.canvas_height:
        #если уперся то всё.
            self.hit_bottom = True
            self.game_over(canvas)
        #вызов функции hit_paddle чтоб проверить не коснулся ли шарик доски
        if self.hit_paddle(pos)==True:
            self.y=-3
        #такая же проверка и на координаты х, чтобы он отскакивал от стен
        if pos[0] <=0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3

    def game_over(self,canvas):
        time.sleep(1)
        canvas.create_text(250,200,text="Game Over", fill='red',font=('Courier',30))


class Paddle:

    def __init__ (self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        #только х, потому что доска не может изменять высоту
        self.x=0
        self.canvas_width=self.canvas.winfo_width()
        self.started = False
        #захват нажатия клавишь для управления доской
        self.canvas.bind_all('<KeyPress-Left>',self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>',self.turn_right)
        self.canvas.bind_all('<Button-1>',self.game_start)


    def draw(self):
        #по игрeку не двигаемся поэтому только x
        self.canvas.move(self.id,self.x,0)
        pos=self.canvas.coords(self.id)
        #доска не отскакивает от стен. она просто упирается и прекращает движение
        if pos[0]<=0:
            #касание левой стены левым верхним углом
            self.x=0
        elif pos[2] >= self.canvas_width:
            #касание правой стены правым нижним углом
            self.x=0
    #эти 2 функции отвечают за движение доски

    def turn_left(self,evt):
        self.x=-2

    def turn_right(self,evt):
        self.x=2

    def game_start(self,evt):
        self.started = True

class Score:
    def __init__(self, canvas, color):
        self.score = 0
        self.canvas = canvas
        self.id = canvas.create_text(450, 10, text=self.score, fill=color)
    def hit(self):
        self.score += 1
        self.canvas.itemconfig(self.id, text=self.score)

tk = Tk()
#имя открытого окна
tk.title("Bounce")
#запрет на растягивание окна
tk.resizable(0,0)
#сделать окно поверх всех окон
tk.wm_attributes("-topmost",1)
#bd=0 - толщина рамки окна 0 пикселей (делаем окно без рамки)
#highlightthickness=0 - подстведка при выбора окна 0 пикселей
canvas=Canvas(tk,width=500,height=400, bd=0,highlightthickness=0)
canvas.pack()
tk.update()
#теперь создадим объект класса Ball - кружок. ball
score = Score(canvas, 'green')
paddle=Paddle(canvas,'blue')
ball=Ball(canvas, paddle, score, 'red')


while 1:
    #проверка касается ли шарик дна.
    if ball.hit_bottom == False and paddle.started == True:
        #вызов функции draw из классов шарика и доски чтоб они нарисовались.
        ball.draw()
        paddle.draw()
        #update и update_idletasks выводят изображения в tkinter на экран
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
