from turtle import *
import random
from math import sqrt
import time
#from colored import fg

start = time.process_time()


def distanc(p1, p2):    
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


#creating canvas
colormode(255)
screen = Screen()
screen.setup(1050,1050)
screen.title('Sierpinks triangle')
screen.bgcolor((0,0,0))





#creating the triangle

height = 500
#max positions
red = (0, height) 
green = (-height, -height)
blue = (height, -height)


#iniciando aleatoriamente um ponto dentro do triangulo
turtle_pos = (random.randint(-150, 150), random.randint(-150, 150))

for i in range(25000):
    dot_turtle = Turtle()
    dot_turtle.hideturtle()  
    dot_turtle.penup()
    dot_turtle.speed(0)
    dot_turtle.goto(turtle_pos)     

    point = random.sample([red, green, blue],1)

    dist_red = distanc(turtle_pos, red)
    dist_green = distanc(turtle_pos, green)
    dist_blue = distanc(turtle_pos, blue)


    min_ = min(dist_red, dist_blue, dist_green)

    r = 0
    g = 0
    b = 0

    if dist_red == min_:
        r = 255        

    else:
        r_ = 2 * height - dist_red
        r = height * r_ / (r_ +height)

    if dist_green == min_:
        g = 255

    else:
        g_ = 2 * height - dist_green
        g = height * g_ / (g_ +height)
  

    if dist_blue == min_:
        b = 255

    else:
        b_ = 2 * height - dist_blue
        b = height * b_ / (b_ +height)
        
    turtle_pos = ((point[0][0] + turtle_pos[0])/2, (point[0][1] + turtle_pos[1])/2)

    r = int(abs(r))
    g = int(abs(g))
    b = int(abs(b))

    print ( ('white')+ str(i) + " / 25000 ", ('red') + str(r), ('green') + str(g), ('blue') + str(b))

    #if you have colored lib installed
    #print ( fg('white')+ str(i) + " / 25000 ", fg('red') + str(r), fg('green') + str(g), fg('blue') + str(b))

    dot_turtle.pendown()
    dot_turtle.dot(3.5, (r,g,b))
    dot_turtle.clone()


print(time.process_time() - start)

screen.mainloop()





    










