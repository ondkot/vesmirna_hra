import pyglet
import math
ROTATION_SPEED = 4
ACCELERATION = 2
presed_keys = []
window = pyglet.window.Window()
class Spaceship:
	def __init__(self):
		self.x = 0
		self.y = 300
		self.x_speed = 0
		self.y_speed = 0
		self.rotation = 0
		self.sprite = pyglet.sprite.Sprite(pyglet.image.load('images\\PNG\\playerShip1_blue.png'))
		self.sprite.x = self.x
		self.sprite.y = self.y
		self.sprite.rotation = 90 - math.degrees(self.rotation)
	def tick(self,dt):
		if pyglet.window.key.UP in presed_keys:
			self.x_speed += dt * ACCELERATION * math.cos(self.rotation)
			self.y_speed += dt * ACCELERATION * math.sin(self.rotation)
		if pyglet.window.key.LEFT in presed_keys:
			self.rotation += dt * ROTATION_SPEED
		if pyglet.window.key.RIGHT in presed_keys:
			self.rotation -= dt * ROTATION_SPEED
		self.x = self.x + dt * self.x_speed
		self.y = self.y + dt * self.y_speed	
		self.sprite.rotation = 90 - math.degrees(self.rotation)
		self.sprite.x = self.x
		self.sprite.y = self.y
	def draw(self):
		self.sprite.draw()
objects = [Spaceship()]
@window.event
def on_draw():
	window.clear()
	for i in objects:
		i.draw()

@window.event
def on_key_press(key_code,modifier):
	if key_code == pyglet.window.key.UP or key_code == pyglet.window.key.LEFT or key_code == pyglet.window.key.RIGHT:
		presed_keys.append(key_code)
@window.event
def on_key_release(key_code,modifier):
	if key_code in presed_keys:
		del presed_keys[presed_keys.index(key_code)]
pyglet.app.run()