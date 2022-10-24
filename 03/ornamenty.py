from turtle import left, right, shape, forward, exitonclick, penup, pendown, back, speed

shape('turtle')
penup()
back(300)
left(90)
pendown()

#ctverec
a = 200

for ctverec in range(10):
    for _ in range(2):
        forward(a - ctverec * 20)
        right(90)

penup()
back(400)
pendown()    

#osmiuhelnik
n = 8
uhel = (180-(180 * (1 - 2/n)))
strana = (800 / n)

for i in range(15):   
    for _ in range(4):
        forward(strana - i*7)
        left(uhel)

left(90)
penup()
forward(400)
pendown()

#spirala
n = 95
uhel = (180-(180 * (1 - 2/n)))
strana = (2 / n)

for i in range(30):   
    for _ in range(42):
        forward(strana + i/4)
        left(uhel)

    

exitonclick()