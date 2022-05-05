from turtle import *
import random


#criando vanvas
colormode(255)
screen = Screen()
screen.setup(1000,1000)
screen.title('Sierpinks triangle')
screen.bgcolor('black')

#
p1 = (0, 250)
p2 = (-250, -250)
p3 = (250, -250)
center = (0,0)

#iniciando aleatoriamente um ponto dentro do triangulo
turtle_pos = (random.randint(-150, 150), random.randint(-150, 150))
colors = ['red', 'blue', 'orange', 'pink', 'white']

for i in range(10000):
    dot_turtle = Turtle()
    dot_turtle.hideturtle()  
    dot_turtle.penup()
    dot_turtle.speed(0)
    dot_turtle.goto(turtle_pos)    
    

    point = random.sample([p1, p2, p3],1)
    dot_color = random.sample(colors,1)

    turtle_pos = ((point[0][0] + turtle_pos[0])/2, (point[0][1] + turtle_pos[1])/2)
    dot_turtle.pendown()
    dot_turtle.dot(3.5, (20, 50, 58))
    dot_turtle.clone()

screen.mainloop()





    










