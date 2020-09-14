"""
print ('Hello World')
a = 'numbers are %s and %s'
b = ''' dfsfdsfds
dsfsdfdsf'''
score = 'a'*5
score2 = 10
print (a % (score, score2))
print ('%s Hello' % score)
print ('%s 1' % score)
print ('%s 2' % score)
print ('%s %s %s Hello' % (score,b,score2))
print (1*'ROW ROW FIGHT DA POWAH ')
"""
#list_ = ['fist','second','third','forth','Simon','Yoko','Buto']
"""
list2 = [1,2,3,4]
print(list)
print(list[2],list[3])
list[0]='Kamina'
print(list[2:5])
list1 = [1,2,3,4,5,list]
print(list1)
list.append('mandrake')
print(list1)
del list[6]
print(list1)
list_sum = list+list2
print(list_sum)
list_tuple=('greetings','treveler')
print(list_tuple)
print(list_tuple[1])
map_test={'A':'Apple',
'B':'Banana',
'C':'Cancer'}
print(map_test)
print(map_test['A'])
del(map_test['A'])
print(map_test)
map_test['B']='Bionicle'
print(map_test)

games=['Warcraft','girls','anime','travel','cooking','gym']
foods=['chicken','olivie salad','cakes','potato','water']
favorits=foods+games
print(favorits)

Fighters=3*25+2*40
print(Fighters)

name='General'
surname='Kenobi'
print('Hi there,',name,surname+'!')

first_name = 'Brando'
last_name = 'Ickett'
print('Hi there, %s %s!' % (first_name, last_name))
"""
#import turtle
#t = turtle.Pen()
#t.reset()
#t.clear()
"""
t.forward(50)
t.left(90)
t.forward(70)
t.left(90)
t.forward(50)
t.left(90)
t.forward(70)
t.left(90)
input()
t.reset()
t.clear()

import math
k1=80
k2=80
g=math.sqrt(math.pow(k1,2)+math.pow(k2,2))
t.forward(k1)
t.left(90)
t.forward(k2)
t.left(135)
t.forward(g)
input()

t.reset()
t.clear()
i=0
while i != 4:
    t.forward(50)
    t.up()
    t.right(45)
    t.forward(50)
    t.right(45)
    t.down()
    i +=1
input()

money = 2000
if money > 1000:
    print("I'm rich!!")
else:
    print("I'm not rich!!")
        print("But I might be later...")

twinkies=501
if twinkies < 100 or twinkies > 500:
    print ('too few or too many')

money = 100
less = 'money %s is between 100 and 500'
huge = 'money %s is between 1000 and 5000'
if money>=100 and money<=500:
    print(less % money)
elif money>=1000 and money<=5000:
    print(huge % money)

toomany='That’s too many'
strugle='It’ll be a struggle, but I can take ’em'
fight='I can fight those ninjas!'
ninjas=20
if ninjas>=30 and ninjas<50:
    print (toomany)
elif ninjas>=10 and ninjas<30:
    print (strugle)
elif ninjas<10:
    print (fight)

ninjas = 5
if ninjas < 10:
print("I can fight those ninjas!")
elif ninjas < 30:
print("It'll be a struggle, but I can take 'em")
elif ninjas < 50:
print("That's too many")

for x in range(0, 5):
    print('hello %s' %x)
print(list(range(10, 20)))
for x in list_:
    print(x)
    for j in list_:
     print(j)

found_coins = 20
magic_coins = 70
stolen_coins = 3
coins = found_coins
for week in range(1, 53):
    coins = coins + magic_coins - stolen_coins
    print('Week %s = %s' % (week, coins))
#1 loop
for x in range(0, 20):
    print('hello %s' % x)
    if x < 9:
        break
#2 loop
age=1
while age <= 29:
    print (age)
    age=age+2
#2 loop alternate
for x in range (1,30,2):
    print(x)

#3 loop
reagents = ['rune of teleportation','rune of portal','arcane powder','light feather','iron grenade']
for i in range (0,5):
  print(i+1, reagents[i])

#4 loop
earth_weight=78
moon_waight="{:.2f}".format(earth_weight*0.165)
print ('starting waight on earth:',earth_weight,'kg')
print('first visit on moon:',moon_waight,'kg')
for x in range (1,16):
    earth_weight=earth_weight+1
    moon_waight="{:.2f}".format(earth_weight*0.165)
    print('year %s - %s' %(x, moon_waight),'kg')
"""
"""
def savings(income,income2,spend):
    return income+income2-spend
print(savings(10,10,5))
def spaceship_building(cans):
    total_cans = 0
    for week in range(1, 53):
        total_cans = total_cans + cans
        print('Week %s = %s cans' % (week, total_cans))
spaceship_building(5)

import sys
def silly_age_joke():
	print('How old are you?')
	age = int(sys.stdin.readline())
	if age >= 10 and age <= 13:
		print('What is 13 + 49 + 84 + 155 + 97? A headache!')
	else:
		print('Huh?')
silly_age_joke()

def moon_weight():
    import math
    import sys
    print ('Please enter your current Earth weight')
    earth_weight= int(sys.stdin.readline())
    print ('Please enter the amount your weight might increase each year')
    weight_gain= int(sys.stdin.readline())
    print ('Please enter the number of years')
    years= int(sys.stdin.readline())
    print ('You will gain +1 kg every year for %s years. your weight on moon should be next:' % years)
    moon_weight="{:.2f}".format(earth_weight*0.165)
    print ('starting waight on earth:',earth_weight,'kg')
    print('first visit on moon:',moon_weight,'kg')
    for x in range (1,years+1):
        earth_weight=earth_weight+weight_gain
        moon_weight="{:.2f}".format(earth_weight*0.165)
        print('year %s - %s' %(x, moon_weight),'kg')
moon_weight()


class Giraffes():
    def left_Foot_Forward(self):
        print('left foot forward')
    def left_Foot_Back(self):
        print('left foot back')
    def right_Foot_Forward(self):
        print('right foot forward')
    def right_Foot_Back(self):
        print('right foot back')
    def dance (self):
        self.left_Foot_Forward()
        self.left_Foot_Back()
        self.right_Foot_Forward()
        self.right_Foot_Back()
        self.left_Foot_Back()
Reginald=Giraffes()
Reginald.dance()


import turtle
t1=turtle.Pen()
t2=turtle.Pen()
t3=turtle.Pen()
t4=turtle.Pen()
t1.forward(100)
t1.left(90)
t1.forward(50)
t1.right(90)
t1.forward(50)
t2.forward(110)
t2.left(90)
t2.forward(20)
t2.right(90)
t2.forward(20)
t3.forward(110)
t3.right(90)
t3.forward(20)
t3.left(90)
t3.forward(20)
t4.forward(100)
t4.right(90)
t4.forward(50)
t4.left(90)
t4.forward(50)
input()

a = abs(10) + abs(-10)
print(a)
b = abs(-10) + -10
print(b)

def Convert(string):
    li = list(string.split(" "))
    return li
str1 = "this if is you not are a reading very this good then way you to have hide done a it message wrong"
list_str1 = Convert(str1)
list_str2=list_str1[::2]
for i in list_str2:
    print(i,end=' ')
"""
"""
filename = input("Enter the name of the file:\n ")
numline = int(input("Enter the number of lines in the file:\n "))
f= open(filename,"w+")
for i in range(0,numline):
    print("enter the %s line"%(i+1))
    line = input()
    f.write(line)
    if i!=(numline-1):
        f.write("\n")
f.close()
import subprocess as sp
programName = "notepad.exe"
sp.Popen([programName, filename])
print ("\nFile %s created! Opening the file...\n"%(filename))
input()

f = open('test.txt')
s = f.read()
f.close()
f = open('output.txt', 'w')
f.write(s)
f.close()
That example works, but actually a better way to copy a file is
using a Python module called shutil:
import shutil
shutil.copy('test.txt', 'output.txt')

class Animal:
    def __init__(self, species, number_of_legs, color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color
import copy
harry = Animal('hippogriff', 6, 'pink')
harriet = copy.copy(harry)
print(harry.species)
print(harriet.species)
carrie = Animal('chimera', 4, 'green polka dots')
billy = Animal('bogill', 0, 'paisley')
my_animals = [harry, carrie, billy]
more_animals = copy.copy(my_animals)
print(more_animals[0].species)
print(more_animals[1].species)
print(more_animals[2].species)

class Animal:
    def __init__ (self, species, number_of_legs, color):
        self.species = species
        self.number_of_legs = number_of_legs
        self.color = color
harry = Animal('hippogriff',6,'pink')
import copy
harriet = copy.copy(harry)
print(harriet.color)
print(harry.color)
carrie = Animal('chimera',4,'green polka dots')
billy = Animal('bogill',0,'paisly')
my_animals = [harry,carrie,billy]
print(my_animals[0].species)
copy_animals = copy.copy(my_animals)
print(copy_animals[0].species)
my_animals[0].species = 'ghoul'
print(my_animals[0].species)
print(copy_animals[0].species,'\n')
sally=Animal('dog',4,'brown')
my_animals.append(sally)
print(len(my_animals))
print(len(copy_animals),'\n')

import time
def lots_of_numbers(max):
    t1 = time.time()
    for x in range(0, max):
        print(x)
    t2 = time.time()
    print('it took %s seconds' %(t2-t1))
lots_of_numbers(1000)

import copy
class Car:
    pass
car1 = Car()
car1.wheels = 4
car2 = car1
car2.wheels = 3
print(car1.wheels)
car3 = copy.copy(car1)
car3.wheels = 6
print(car1.wheels)

import pickle
import time
fav_things = ["lego","warcraft","friends"]
save_file = open('save.txt','wb')
pickle.dump(fav_things,save_file)
save_file.close()
time.sleep(2)
load_file=open('save.txt','rb')
load_fav_things=pickle.load(load_file)
print(load_fav_things)

import turtle
import time
t = turtle.Pen()
t.reset()
def mycircle(r,g,b,x):
    t.color(r,g,b)
    t.begin_fill()
    t.circle(x)
    t.end_fill()
    input()
def mysquare(size,filled):
    if filled == True:
        t.begin_fill()
    for x in range(1, 5):
        t.forward(size)
        t.left(90)
    if filled == True:
        t.end_fill()
    input()
def mystar(size,filled):
    if filled == True:
        t.begin_fill()
    for x in range (1,19):
        t.forward(size)
        if x % 2 == 0:
            t.left(175)
        else:
            t.left(225)
    if filled == True:
        t.end_fill()
    input()
#задача 11.1 и 11.2
def myoctagon(size,filled,shaped):
    if filled == True:
        t.begin_fill()
    for x in range (1,9):
        t.forward(size)
        t.left(45)
    if filled == True:
        t.end_fill()
    if shaped == True:
        t.color(0,0,0)
        myoctagon(size,0,0)
    input()

#задача 11.3
#у меня вышла тупоконечная звезда, по факту тоже звезда)
def draw_star(size, a):
    x = 180/a
    y = 540/a
    for i in range (1,a*2+1):
        t.forward(size)
        if i % 2 == 0:
            t.right(x)
        else:
            t.left(y)
    input()
#а в ответе остроконечная (180-х) я это не учел
def draw_star1(size, points):
    angle = 360 / points
    for x in range(0, points):
        t.forward(size)
        t.left(180 - angle)
        t.forward(size)
        t.right(180-(angle * 2))
    input()
"""
#глава 12
from tkinter import *
import random
def hello():
    print('hello there')
def random_rectange(width,height,number):
    for x in range(0, number):
        x1=random.randrange(width)
        y1=random.randrange(height)
        x2=x1+random.randrange(width)
        y2=y1+random.randrange(height)
        canvas.create_rectangle(x1,y1,x2,y2)
tk=Tk()
btn = Button(tk,text="click me",command=hello)
#btn.pack()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()
#canvas.create_line(0,0,500,500)
#canvas.create_rectangle(10,10,50,50)
random_rectange(400,400,100)
input()
