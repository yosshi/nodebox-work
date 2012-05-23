from AppKit import NSShadow, NSColor
from nodebox.graphics import Grob
 
class shadow(Grob):
    def __init__(self, x=10, y=10, alpha=0.25, blur=4.0):
        Grob.__init__(self, _ctx)
        self._shadow = NSShadow.alloc().init()
        self._shadow.setShadowOffset_((x, -y))
        self._shadow.setShadowColor_(color(0, 0, 0, alpha)._rgb)
        self._shadow.setShadowBlurRadius_(blur)
        self.draw()
    def _draw(self):
        self._shadow.set()
        
def noshadow():
    shadow(alpha=0)
# --------------------------
    
size(800,500)
words = [u"にゅるにゅる",
         u"大学で作業しなければならなくなったら、せめてハードディスク容量だけはなんとかしたいので、私物の外付けハードディスクを持ち込むだあな。メモリはどうにもならんが",
         u"いや、違うか。免許取れるのって18だっけ。21だ。これ。",
         u"去年じゃねえか。",
         u"地元の連中は平気で当日に連絡よこしたりするから気は抜けないが。",
         u"まあ一応就職活動が控えていたというのもあったけど。でも1社で終わったし茶髪でも問題なかったと思う。常に半ズボンだし。",
         u"trapezoid_is_otake",
         u"WBSの特集みてる。金融不動産不安の中で、今年の秋の東京大型都心マンションの売れ行きは？"]
colors = [color(1,0,0), color(1,1,1), color(0,0,0)]
ftype = ["Hiragino Mincho Pro W3",
         "Hiragino Mincho Pro W6",
         "Hiragino Kaku Gothic Pro",
         "Hiragino Kaku Gothic Std",
         "Hiragino Maru Gothic Pro",
         "Osaka"]

for i in range(100):
    shadow(x=0,y=10,alpha=0.5,blur=5)
    x = 0
    y = random(HEIGHT*1.3)
#    rotate(random(360))
    fontsize(random(10,100))
 
#    fill(choice(colors))
    color_value = random(0,0.99999999)
    c = color(color_value,color_value,color_value)
#    c = color(random(0,0.9), random(0,0.3), random(0,0.3))

    fill(c)
    font(choice(ftype))
    text(choice(words), x, y)

# twitter
fill(color(0.1,0.9,0.9))
font("Silom")
fontsize(120)
text("twitter", 300, 490)

