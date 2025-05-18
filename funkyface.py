from turtle import *

class Face:

    def __init__(self, xpos, ypos):
        self.size = 90
        self.coord = (xpos, ypos)
        self.noseSize = 'small'

    def setSize(self, radius):
        self.size = radius

    def draw(self):
        self.goHome()
        pensize(3)
        speed(0)
        self.drawOutLine()
        self.drawEye(135)
        self.drawEye(45)
        self.drawMouth()
        self.drawNose()
        pensize(5)

# --------------------------------------------------
#    Functions that are calles from with the class
# --------------------------------------------------


    # After drawing each part, turtle position
    # returns to centre. Parts can be drawn in any order.
    def goHome(self):
        penup()
        goto(self.coord)

        setheading(0)

    def drawOutLine(self):
        penup()
        # move turtle pen in forward direction
        forward(self.size)
        left(90)
        # draw a circle of given radius
        pendown()
        circle(self.size)
        # return back to centre
        self.goHome()

    def drawEye(self, turn):
        penup()
        # turn turtle pen to given angle
        left(turn)
        # move turtle pen in forward direction
        forward(self.size / 2)
        pendown()
        # draw a circle of given radius
        dot(self.size/10)
        # return back to centre
        # self.goHome()
    def drawMouth(self):
        penup()
        # turn turtle pen to given angle
        # right(135)
        # move turtle pen in forward direction
        forward(self.size/1.7)
        left(90)
        pendown()
        # draw a circle of given radius
        # but till given extent only
        circle(self.size/1.7,90)
        self.goHome()

    def drawNose(self):
        if self.noseSize == 'large':
            dot(self.size/2, "grey")
        elif self.noseSize == 'small':
            dot(self.size/6, "grey")
        else:
            dot(self.size/4, "grey")
        self.goHome()


# start of drawing code
# ---------------------

f1 = Face(0, 0)
f1.draw()

showturtle()
done()