from turtle import fillcolor, begin_fill, forward, left, end_fill, exitonclick

size = 100
color = "purple"

#Nastavit barvu
fillcolor(color)
begin_fill()

#Nakresli ctverec
for _ in range(4):
    forward(size)
    left(90)

end_fill()

exitonclick()
