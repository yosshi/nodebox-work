width = 1920
height =1200

size(width, height)
speed(2)
grid_width  = 2
grid_height = height 

color_value = 0
c = color(color_value, color_value,color_value)
fill(c)
rect(0,0, width, height)


def draw():
    for x, y in grid(width/grid_width,height/grid_height, grid_width, grid_height):
        push()
        # Scale every element from 20% to 120% of its original size.
        #scale(random(1,1))
        # Draw an oval that is a little bit smaller than the row and
        # column width.

        color_value = random(0.5,1.555555555555)
#        c = color(color_value, color_value,color_value)
        c = color(random(0,0.5), random(0,0.3),random(0,0.2))
        fill(c)
        rect(x*random(1,10),y, grid_width*random(0,100), grid_height)

#        color_value = random(0,0.9)
#        c = color(color_value, color_value,color_value)
#        fill(c)
#        oval(x,y, grid_width, grid_width)


        pop()

