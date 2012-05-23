from AppKit import NSShadow, NSColor
from nodebox.graphics import Grob
 
class shadow(Grob):
    def __init__(self, x=10, y=10, alpha=0.25, blur=4.0,red=0,green=0,blue=0):
        Grob.__init__(self, _ctx)
        self._shadow = NSShadow.alloc().init()
        self._shadow.setShadowOffset_((x, -y))
        self._shadow.setShadowColor_(color(red, green, blue, alpha)._rgb)
        self._shadow.setShadowBlurRadius_(blur)
        self.draw()
    def _draw(self):
        self._shadow.set()
        
def noshadow():
    shadow(alpha=0)
# --------------------------
from math import sin, cos,pi
size(1920,1200)
background(color(0,0,0.2))
r = 350
x = 400
y = 800
per = 10

for i in range(360):
    r= i*15
    shadow(x=0,y=0,alpha=1,blur=100,blue=0.7,green=0.1)
    fill(color(0.0,0.0,0.2))
    font("Silom")
    fontsize(40)
    t= text("twitter", x+sin(per*i*pi/180)*r, y+cos(per*i*pi/180)*r)
    t.rotate(-90+i*per)



for i in range(360):
    r= i*10
    shadow(x=0,y=0,alpha=1,blur=100,blue=0.7,green=0.1)
    fill(color(0.1,0.9,0.9))
    font("Silom")
    fontsize(40)
    t= text("twitter", x+sin(per*i*pi/180)*r, y+cos(per*i*pi/180)*r)
    t.rotate(-90+i*per)





shadow(x=0,y=0,alpha=1,blur=100,blue=1,green=0.5)
fill(color(1,1,1))
font("Impact")
fontsize(20)
for z in range(5):
    for i in range(35):
        text("twitter", i*60, z*30+200)

