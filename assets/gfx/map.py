import pyglet 
win = pyglet.window.Window()


img = pyglet.image.load('assets/gfx/Inner.png')


def update(dt):
    pass
    
sprites = []
for i in range(4):
    for j in range(4):
        sprites.append(pyglet.sprite.Sprite(img, x = i, y = j))


def on_draw():
    for i in range(4):
        sprites[i].draw()



pyglet.clock.schedule(update) 
pyglet.app.run()