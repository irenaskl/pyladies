import random
from turtle import left, right, shape, forward, exitonclick, penup, pendown, back, setposition, speed, goto
import math

speed(0)
shape('turtle')
penup()
back(400)
right(90)
forward(300)
left(90)
pendown()

#vesnice
#strana domecku = a
a = 70
odmocnina = math.sqrt(2)

for domecek in range(7):
    for strana in range(1):
        for _ in range(2):
            forward(a)
            left(90)
        forward(a)
        right(135)
    for _ in range(2):
        forward(odmocnina * a / 2)
        right(90)
    forward(odmocnina * a)
    right(135)
    forward(a)
    right(135)
    forward(odmocnina * a)

    left(45)
    forward(50)

penup()
left(90)
forward(500)
left(45)
pendown()

#hory
for hora in range(3):
    #kazda hora se zvetsi 80krat)
    forward(130 + hora*80)
    left(90)
    forward(130 + hora*80)
    right(90)

penup()
left(135)
forward(200)
left(90)
pendown()

#les
for strom in range(7):
    left(45)
    forward(50)
    left(135)
    forward(20)
    right(135)
    forward(40)
    left(135)
    forward(10)
    right(135)
    forward(40)

    right(90)
    forward(40)
    right(135)
    forward(10)
    left(135)
    forward(40)
    right(135)
    forward(20)
    left(135)
    forward(50)
    left(45)

penup()
left(90)
forward(300)
right(90)
pendown()

#vlocky
vlocka_cara = 20
vlocka_spicka = 7

#Premku, jestli jsi cetl tento kod,
#napis mi do slacku "ano" :-)
for vlocka in range(20):
    for cara in range(8):
        left(90)
        forward(vlocka_cara)
        back(vlocka_spicka)
        left(45)
        forward(vlocka_spicka)
        back(vlocka_spicka)
        right(90)
        forward(vlocka_spicka)
        back(vlocka_spicka)
        left(45)
        back(vlocka_cara - vlocka_spicka)
        left(45)
    x = random.randint(-250,250)
    y = random.randint(-250,250)
    penup()
    goto(x, y)
    pendown()

exitonclick() 







