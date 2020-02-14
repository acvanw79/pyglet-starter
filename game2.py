import pyglet

win= pyglet.window.Window()

# Create a sprite so the game can keep track of coordinates
img= pyglet.image.load('assets/hero/sliced/idle-3.png')
spr = pyglet.sprite.Sprite(img, x = 200, y = 200)

spritesheet= pyglet.image.load('assets/hero/Old hero.png')
smol_img = pygame.Surface([16, 16])
smol_img.blit(spritesheet, (0, 0), (16, 0, 16, 16))

# Get the key state handler object
keys = pyglet.window.key.KeyStateHandler()

def update(dt):
    win.push_handlers(keys)             # update the keys object
    if keys[pyglet.window.key.LEFT]: # if the key is pressed...
        spr.x -= 1                                # change spr.x by -1
    if keys[pyglet.window.key.RIGHT]:
        spr.x += 1
    if keys[pyglet.window.key.UP]:
        spr.y += 1
    if keys[pyglet.window.key.DOWN]:
        spr.y -= 1

@win.event
def on_draw():
    win.clear()
    spr.draw()

pyglet.clock.schedule(update) 
pyglet.app.run()