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