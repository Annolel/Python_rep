from tkinter import *
import random
import time
class Ball:
    def __init__(self,canvas,color):
        self.canvas=canvas
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
        #если уперся он движется опять вверх
            self.y=-3
        #такая же проверка и на координаты х, чтобы он отскакивал от стен
        if pos[0] <=0:
            self.x=3
        if pos[2]>=self.canvas_width:
            self.x=-3
class Paddle:
    def __init__ (self,canvas,color):
        self.canvas=canvas
        self.id=canvas.create_rectangle(0,0,100,10,fill=color)
        self.canvas.move(self.id,200,300)
        #только х, потому что доска не может изменять высоту
        self.x=0
        self.canvas_width=self.canvas.winfo_width()
    def draw(self):
        pass
    #эти 2 функции отвечают за движение доски
    def turn_left(self,evt):
        self.x=-2
    def turn_right(self,evt):
        self.x=2
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
ball=Ball(canvas,'red')
paddle=Paddle(canvas,'blue')
while 1:
    #вызов функции draw из классов шарика и доски чтоб они нарисовались.
    ball.draw()
    paddle.draw()
    #update и update_idletasks выводят изображения в tkinter на экран
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
