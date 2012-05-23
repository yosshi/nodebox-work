width = 320
height =480

size(width, height)
grid_width  = width
grid_height = 2

color_value = 0
c = color(color_value, color_value,color_value)
fill(c)
rect(0,0, width, height)


for x, y in grid(width/grid_width,height/grid_height, grid_width, grid_height):
    push()
    # Scale every element from 20% to 120% of its original size.
    #scale(random(1,1))
    # Draw an oval that is a little bit smaller than the row and
    # column width.

    color_value = random(0.5,1.555555555555)
#    c = color(color_value, color_value,color_value)
    c = color(random(0,0.5), random(0,0.3),random(0,0.2))
    fill(c)
    rect(x, y*random(1,10), grid_width, grid_height*random(0,100))
#        color_value = random(0,0.9)
#        c = color(color_value, color_value,color_value)
#        fill(c)
#        oval(x,y, grid_width, grid_width)
    pop()

