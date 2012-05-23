width = 1920
height =1200

size(width, height)
# Nauseating grid of circles.
# Each circle is randomly enlarged or shrinked a little bit,
# so it looks like a really blown up raster image.
# "What do you see?"

grid_width  = 60
grid_height = 60 

color_value = 1
c = color(color_value, color_value,color_value)
fill(c)
rect(0,0, width, height)



for x, y in grid(width/grid_width,height/grid_height, grid_width, grid_height):
        push()
        # Scale every element from 20% to 120% of its original size.
        #scale(random(1,1))
        # Draw an oval that is a little bit smaller than the row and
        # column width.

        color_value = random(0,0.555555555555)
        c = color(color_value, color_value,color_value)
        fill(c)
        rect(x,y, grid_width-10, grid_height-10)

#        color_value = random(0,0.9)
#        c = color(color_value, color_value,color_value)
#        fill(c)
#        oval(x,y, grid_width, grid_width)


        pop()

