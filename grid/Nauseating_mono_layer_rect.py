size(1920, 1200)
# Nauseating grid of circles.
# Each circle is randomly enlarged or shrinked a little bit,
# so it looks like a really blown up raster image.
# "What do you see?"


#speed(30)

# Create a grid of 20 by 20. Each row and column is 30 points.
#def draw():
color_value = 0.2
c = color(color_value, color_value,color_value)
fill(c)
rect(0, 0,1920,1200)

for x, y in grid(9,40,30,30):
        push()
        # Scale every element from 20% to 120% of its original size.
        #scale(random(1,1))
        # Draw an oval that is a little bit smaller than the row and
        # column width.

        color_value = random(0,0.9)
        c = color(color_value, color_value,color_value)
        fill(c)
        rect(x,y,30,30)

#        color_value = random(0,0.9)
        color_value = color_value * 1.2
        c = color(color_value, color_value,color_value)
        fill(c)
        rect(x+5,y+5,20,20)

#        color_value = random(0,0.9)
        color_value = color_value * 1.2
        c = color(color_value, color_value,color_value)
        fill(c)
        rect(x+10,y+10,10,10)



        pop()
