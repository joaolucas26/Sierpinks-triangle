from turtle import *
import random
from math import sqrt
import time
#from colored import fg

start = time.process_time()
TOTAL_POINTS = 25000
MAX_VALUE = 255
MIN_VALUE = 0

#creating canvas
colormode(255)
screen = Screen()
screen.setup(1050,1050)
screen.title('Sierpinks triangle')
screen.bgcolor((0,0,0))

#creating the triangle
HEIGHT = 500
#max positions
RED = (0, HEIGHT) 
GREEN = (-HEIGHT, -HEIGHT)
BLUE = (HEIGHT, -HEIGHT)


def distanc(p1, p2):    
    return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


#iniciando aleatoriamente um ponto dentro do triangulo
TURTLE_POS = (random.randint(-150, 150), random.randint(-150, 150))

for i in range(TOTAL_POINTS):
    dot_turtle = Turtle()
    dot_turtle.hideturtle()  
    dot_turtle.penup()
    dot_turtle.speed(0)
    dot_turtle.goto(TURTLE_POS)     

    point = random.sample([RED, GREEN, BLUE],1)

    dist_red = distanc(TURTLE_POS, RED)
    dist_green = distanc(TURTLE_POS, GREEN)
    dist_blue = distanc(TURTLE_POS, BLUE)


    min_ = min(dist_red, dist_blue, dist_green)

    r = 0
    g = 0
    b = 0

    if dist_red == min_:
        r = MAX_VALUE        

    else:
        r_ = 2 * HEIGHT - dist_red
        r = HEIGHT * r_ / (r_ +HEIGHT)

    if dist_green == min_:
        g = MAX_VALUE

    else:
        g_ = 2 * HEIGHT - dist_green
        g = HEIGHT * g_ / (g_ +HEIGHT)
  

    if dist_blue == min_:
        b = MAX_VALUE

    else:
        b_ = 2 * HEIGHT - dist_blue
        b = HEIGHT * b_ / (b_ +HEIGHT)
        
    TURTLE_POS = ((point[0][0] + TURTLE_POS[0])/2, (point[0][1] + TURTLE_POS[1])/2)

    r = int(abs(r))
    g = int(abs(g))
    b = int(abs(b))

    print (f'{i}/{TOTAL_POINTS} - COLOR: ({r},{g}. {b}) - POINT: X:{round(TURTLE_POS[0], 2)}, Y:{round(TURTLE_POS[1], 2)}')

    #if you have colored lib installed
    #print ( fg('white') + str(i) + " / 25000 ", fg('red') + str(r), fg('green') + str(g), fg('blue') + str(b))

    dot_turtle.pendown()
    dot_turtle.dot(3.5, (r,g,b))
    dot_turtle.clone()


print(time.process_time() - start)

screen.mainloop()





    










