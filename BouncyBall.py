from vpython import*
from time import*
ceiling=box(color=color.white,pos=vector(0,2.5,0), size=vector(5.1,.1,5))
floor=box(color=color.white, pos=vector(0,-2.5,0), size=vector(5.1,.1,5))
wall1=box(color=color.white, pos=vector(0,0,-2.5), size=vector(5.1,5.1,.1))
wall2=box(color=color.white, pos=vector(-2.5,0,0), size=vector(.1,5,5))
wall3=box(color=color.white, pos=vector(2.5,0,0),  size=vector(.1,5,5))
marble=sphere(color=color.green, radius=.5)
deltaX=.001
xPos=0

while True:
    rate(1000)
    xPos=xPos+deltaX
    if (xPos>1.9 or xPos<-1.9):
        deltaX=deltaX*(-1)
    marble.pos=vector(xPos,0,0)
