size(1920, 1200)
# Nauseating grid of circles.
# Each circle is randomly enlarged or shrinked a little bit,
# so it looks like a really blown up raster image.
# "What do you see?"

# Create a grid of 20 by 20. Each row and column is 30 points.
for x, y in grid(64,40,30,30):
        push()
        # Scale every element from 20% to 120% of its original size.
        #scale(random(1,1))
        # Draw an oval that is a little bit smaller than the row and
        # column width.
        color_value = random(0,0.9)
        c = color(color_value, color_value,color_value)
        fill(c)
        oval(x,y,30,30)
        pop()
