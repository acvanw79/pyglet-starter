import pyglet # import the library
window = pyglet.window.Window() # create the window

# Create some text
label = pyglet.text.Label('Hello erabody', x = 200, y = 200)

# inside the loop:
def on_draw():
    text.draw()
    
# label = pyglet.text.Label('Hello, world', x = 200, y = 200)



# Create a sprite
ball_image = pyglet.image.load('assets/hero/Old hero.png')
ball = pyglet.sprite.Sprite(ball_image, x=50, y=50)


def update(dt):
    ball.x += 0.5
    ball.y += 0.5

# Start the event loop
@window.event
def on_draw():
    window.clear()
    ball.draw()



pyglet.clock.schedule(update)
pyglet.app.run()