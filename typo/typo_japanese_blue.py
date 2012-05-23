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
size(1000,900)
twitter_blue = color(0.1,0.9,0.9) 
background(twitter_blue)
words = [u"http://twitter.com",
         u"「いま何してる？」",
         u"最適化の極意は「どれだけ速く計算するか」ではなく「どれだけ計算をせずに済ますか」",
         u"「日本は今欧米の若者にとって、超ミステリアスでクールな聖地となりつつある」",
         u"通堂のもやしレシピをメモってきた。 ",
         u"そういえば、昨日は ekワゴン青の痛車をみた。 ",
         u"ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。ねむす。",
         u"これなら金属アレルギーでも大丈夫",
         u"もう11時！",
         u"gmail でいいですか",
         u"メルアドかえるかー",
         u"32GB に \"64GB\" って刻印しよう。",
         u"これのおかげで、Gmailからメール転送できなくなりました。ありがとうございました。"]
colors = [color(1,0,0), color(1,1,1), color(0,0,0)]
ftype = ["Hiragino Mincho Pro W3",
         "Hiragino Mincho Pro W6",
         "Hiragino Kaku Gothic Pro",
         "Hiragino Kaku Gothic Std",
         "Hiragino Maru Gothic Pro",
         "Osaka"]
for i in range(WIDTH/2):
    shadow(x=0,y=0, alpha=0.5,blur=50)
    fill(twitter_blue)
#    fill(color(random(0,0.1), random(0.4,0.9), random(0.8,0.9)))
    x = random(-1*WIDTH,WIDTH)
    y = random(HEIGHT*1.3)
    #r = text(words[i], x, y)
    r = text(choice(words), x, y)
    r.rotate(random(-45,45))
    fontsize(random(10,100)) 
    font(choice(ftype))

# twitter
shadow(x=0, y=0, alpha=0.9, blur=100, blue=0.5)
fill(color(1,1,1))
font("Silom")
fontsize(120)
text("twitter", WIDTH-500, HEIGHT-10)
