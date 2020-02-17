import pyglet

win= pyglet.window.Window()

hp = 100

# Create a sprite so the game can keep track of coordinates
img= pyglet.image.load('assets/hero/sliced/idle-3.png')
spr = pyglet.sprite.Sprite(img, x = 200, y = 200)

img2 = pyglet.image.load('assets/forest-assets/cave.png')

spritesheet= pyglet.image.load('assets/hero/Old hero.png')

# create some texe
tittle = pyglet.text.Label('Mr. Fantastic', x = 275, y = 465)
text = pyglet.text.Label(text = "100", x = 0, y = 465)



# Get the key state handler object
keys = pyglet.window.key.KeyStateHandler()

def update(dt):
    global hp
    text.text = str(hp)
    print(hp)
    win.push_handlers(keys)             # update the keys object
    if keys[pyglet.window.key.LEFT]: # if the key is pressed...
        spr.x -= 1                                # change spr.x by -1
    if keys[pyglet.window.key.RIGHT]:
        spr.x += 1
    if keys[pyglet.window.key.UP]:
        spr.y += 1
    if keys[pyglet.window.key.DOWN]:
        spr.y -= 1
    if spr.x < 0:
        hp -= 1
    if spr.x > 630:
        hp -= 1
    if spr.y < 0:
        hp -= 1
    if spr.y > 470:
        hp -= 1


@win.event
def on_draw():
    win.clear()
    if hp > 0:
        spr.draw()
    text.draw()
img.blit(x = 100, y = 100)
    

pyglet.clock.schedule(update) 
pyglet.app.run()
