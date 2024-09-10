
class Rolls:
    def __init__(self, rectwidth, rectheight):
        self.rectwidth = rectwidth
        self.rectheight = rectheight
        self.angle = 0
        self.x = 0
        self.y = 0

    def draw_rolls(self, adj):

        g = (map(self.y, 0, 600, 0, 255) + random(-20, 20)) + adj / 4
        r = (map(self.y, 0, 600, 0, 255) + random(-20, 20)) + adj / 4
        b = (map(self.x, 0, 600, 0, 255) + random(-20, 20)) + adj / 4


        self.x = 600 / 2 + (cos(radians(self.angle)) * self.rectwidth) / 2 - self.x / 16
        self.y = 600 / 2 + (sin(radians(self.angle)) * self.rectheight) / 2 - self.y / 16

        stroke(r, g, b)
        print(r,g,b)
        rect(self.x + adj, self.y + adj, self.rectheight, self.rectwidth)
        rect(self.y + adj, self.x + adj, self.rectwidth, self.rectheight)

        self.angle += 4
        if self.angle > 360:
            self.angle = 0

        # Draw ellipse
        ellipse(self.x + adj, self.y + adj, 40, 40)

def setup():
    size(600, 600)
    #angleMode(DEGREES)
    #rectMode(CENTER)
    background(0)
    global moving_roll, moving_roll2
    #stroke(0,255,0)
    noFill()
    moving_roll = Rolls(60, 180)
    moving_roll2 = Rolls(60, 1200)

def draw():
    moving_roll.draw_rolls(0)
    moving_roll.draw_rolls(200)
    moving_roll.draw_rolls(-200)
    
