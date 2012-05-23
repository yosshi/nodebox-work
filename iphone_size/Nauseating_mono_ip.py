size(320, 480)
# Nauseating grid of circles.
# Each circle is randomly enlarged or shrinked a little bit,
# so it looks like a really blown up raster image.
# "What do you see?"

# Create a grid of 20 by 20. Each row and column is 30 points.
twitter_blue = color(0.0,0.0,0.0) 
background(twitter_blue)

for x, y in grid(64,40,30,30):
    push()
    color_value = random(0,0.9)
    c = color(color_value, color_value,color_value)
    fill(c)
    oval(x,y,20,20)
    pop()
