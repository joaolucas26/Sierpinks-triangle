from turtle import *
import random


#criando vanvas
screen = Screen()
screen.setup(750,750)
screen.title('koch snowflake')
screen.bgcolor('black')

#
p1 = (-125, 250)
p2 = (125, 250)
p3 = (250, 0)
p4 = (125,-250)
p5 = (-125,-250)
p6 = (-250,0)
center = (0,0)


t = Turtle()
t.hideturtle()
t.color('white')
t.speed(0)
t.penup()
t.setposition(p1)
t.pendown()
t.goto(p2) 

t = Turtle()
t.hideturtle()
t.color('white')
t.speed(0)
t.penup()
t.setposition(p2)
t.pendown()
t.goto(p3) 

t = Turtle()
t.hideturtle()
t.color('white')
t.speed(0)
t.penup()
t.setposition(p3)
t.pendown()
t.goto(p4) 

t = Turtle()
t.hideturtle()
t.color('white')
t.speed(0)
t.penup()
t.setposition(p4)
t.pendown()
t.goto(p5) 

t = Turtle()
t.hideturtle()
t.color('white')
t.speed(0)
t.penup()
t.setposition(p5)
t.pendown()
t.goto(p6) 


t = Turtle()
t.hideturtle()
t.color('white')
t.speed(0)
t.penup()
t.setposition(p6)
t.pendown()
t.goto(p1) 




#iniciando aleatoriamente um ponto dentro do hexagono
dot_pos = (random.randint(-100, 100), random.randint(-100, 100))



for i in range(10000):
    print(i, "/9999")
    dot_turtle = Turtle()
    dot_turtle.hideturtle()  
    dot_turtle.penup()
    dot_turtle.speed(0)
    dot_turtle.goto(dot_pos) 
    

    point_a = random.sample([p1, p2, p3, p4, p5, p6],1)

    if (point_a[0] == p1):
        point_b =  random.sample([p2, p6],1)

    if (point_a[0] == p2):
        point_b =  random.sample([p1, p3],1)

    if (point_a[0] == p3):
        point_b =  random.sample([p2, p4],1)
        

    if (point_a[0] == p4):
        point_b =  random.sample([p5, p3],1)

    if (point_a[0] == p5):
        point_b =  random.sample([p4, p6],1)

    if (point_a[0] == p6):
        point_b =  random.sample([p5, p1],1)


    # t = Turtle()
    # t.setposition(dot_pos)
    # t.goto(point_a[0])

    # t = Turtle()
    # t.setposition(dot_pos)
    # t.goto(point_b[0])


    dot_color = 'white'
    dot_pos = ((point_a[0][0] + dot_pos[0] + point_b[0][0])/3, (point_a[0][1] + dot_pos[1] + point_b[0][1])/3)

    
    # t = Turtle()
    # t.setposition(dot_pos)

    #dot_turtle.pendown()
    dot_turtle.dot(3.5, 'white')
    #dot_turtle.clone()

screen.mainloop()





    










