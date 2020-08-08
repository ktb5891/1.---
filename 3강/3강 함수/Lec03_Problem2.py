import turtle
import random
turtle.title('거북이 그리기')
turtle.shape('turtle')
turtle.pensize(3)
turtle.setup(width =330, height =330)
turtle.screensize(300,300)

for i in range(1, 80):
    turtle.pencolor(random.random(),random.random(),random.random())
    turtle.forward(5+i)
    turtle.left(30)

turtle.done()