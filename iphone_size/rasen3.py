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
size(320, 480)
background(color(0,0,0))
x = 140
y = 260
per = 13


for i in range(560):
    r= i* 0.57
    shadow(x=0,y=-20,alpha=0.2,blur=50,red=1,blue=1,green=1)
    fill(color(0.1,0.1,0.1))
    font("Silom")
    fontsize(40)
    t= text(u"螺旋", x+sin(per*i*pi/180)*r, y+cos(per*i*pi/180)*r)
    t.rotate(-90+i*per)

