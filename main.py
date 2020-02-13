import pyglet # import the library
win= pyglet.window.Window() # create the window
keys = pyglet.window.key.KeyStateHandler()
# Create a sprite

if keys[key.SPACE]:
  print("Spacebar pressed!")
if keys[key.UP]:
  print("Up key pressed!)

spr = pyglet.sprite.Sprite(img, x = 200, y = 200)
spr.draw()


img= pyglet.image.load('assets/hero/Old hero.png')

img= pyglet.image.load('assets/hero/sliced/surprise.png')

cva= pyglet.image.load('assets/gfx/cave.png')

afs= pyglet.image.load('assets/gfx/Overworld.png')

def update(dt):
  win.push_handlers(keys) # update the key object
if keys[key.LEFT]:
  print("left key pressed")
  spr.x -= 1
if keys[key.RIGHT]:
  spr.x += 1

# Start the event loop
@win.event
def on_draw():
    win.clear()
    img.blit(100, 150)
    afs.blit(100000, 100000)
    cva.blit(200000, 200000)

pyglet.clock.schedule(update) 
pyglet.app.run()