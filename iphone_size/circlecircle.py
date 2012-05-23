size(320, 480)
# Nauseating grid of circles.
# Each circle is randomly enlarged or shrinked a little bit,
# so it looks like a really blown up raster image.
# "What do you see?"

# Create a grid of 20 by 20. Each row and column is 30 points.
bgcolor = color(1,1,1) 
background(bgcolor)


color_value = random(0,0.9)
black = color(0,0,0)
white = color(1,1,1)
gray  = color(0.5,0.5,0.5)


speed(2)
def draw():
    for i in range(24):
        x = random(-10,320)
        y = random(-10,480)
        s=random(40,150)
        fill(black)
        oval(x,y,s,s)
        fill(white)
        oval(x+5,y+5,s-10,s-10)
        fill(black)
        oval(x+10,y+10,s-20,s-20)
        fill(gray)
        oval(x+15,y+15,s-30,s-30)
        fill(black)
        oval(x+20,y+20,s-40,s-40)
