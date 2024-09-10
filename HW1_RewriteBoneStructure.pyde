## this sketch is from my homework from creaetive coding class https://editor.p5js.org/nalmbaid/sketches/hp1QjH_xf

import math
def setup():
    size(700,700)
    background(0)
    noFill()
    #angleMode(DEGREES)

x1 = 0
x2 = 0
y1 = 0
y2 = 0
speed1 = 3
speed2 = 5
rotation = math.radians(0)
def draw():
    global x1,x2,y1,y2,speed1,speed2,rotation
    stroke(255,255,255,x1)
    translate(x1,y1)
    rotate(rotation)
    ellipse(0, 0, 100, 50)
    x1 = x1 + speed1
    #print(x1)
    y1 = y1 + speed2
    resetMatrix()

    translate(x2,y2)
    rotate(-rotation)
    ellipse(0,5,100,50)
    x2 = x2+ speed2
    y2 = y2+ speed1
    
    rotation = rotation + math.radians(5)
    
    resetMatrix()

    
    
