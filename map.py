import pyglet 
win = pyglet.window.Window()


img = pyglet.image.load('assets/gfx/Inner.png')
smol_img = img.get_region(x=16, y=16, width=64, height=64)

def update(dt):
    pass
    
sprites = []
for i in range(4):
    for j in range(4):
        sprites.append(pyglet.sprite.Sprite(smol_img, x = i, y = j))



def on_draw():
    sprites[i].draw()


pyglet.clock.schedule(update) 
pyglet.app.run()