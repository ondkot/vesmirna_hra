import pyglet
import math
import random
ROTATION_SPEED = 4
ACCELERATION = 10
numbers = []
window = pyglet.window.Window()
path = "images\\PNG\\UI\\"
for i in range(10):
	file = "numeral" + str(i) + ".png"
	numbers.append(pyglet.sprite.Sprite(pyglet.image.load(path + file)))
	numbers[i].y = window.height - 60
	numbers[i].scale = 2
presed_keys = []
class globalni():
	def __init__(self):
		self.promena = ""
class GameOver:
	def __init__(self):
		self.sprite = pyglet.sprite.Sprite(pyglet.image.load("images\\gameover.png"))
	def tick(self,dt):
		pass
	def draw(self):
		self.sprite.draw()
class Spaceship:
	def __init__(self):
		self.laser = 0.9
		self.x = 0
		self.y = 300
		self.x_speed = 0
		self.y_speed = 0
		self.rotation = 0
		image = pyglet.image.load('images\\PNG\\playerShip1_blue.png')
		image.anchor_x = image.width // 2
		image.anchor_y = image.height // 2
		self.sprite = pyglet.sprite.Sprite(image)
		self.sprite.x = self.x
		self.sprite.y = self.y
		self.sprite.rotation = 90 - math.degrees(self.rotation)

	def tick(self,dt):
		if pyglet.window.key.UP in presed_keys:
			self.x_speed += dt * ACCELERATION * math.cos(self.rotation)
			self.y_speed += dt * ACCELERATION * math.sin(self.rotation)
		if pyglet.window.key.DOWN in presed_keys:
			self.x_speed -= dt * ACCELERATION * math.cos(self.rotation)
			self.y_speed -= dt * ACCELERATION * math.sin(self.rotation)
		if pyglet.window.key.LEFT in presed_keys:
			self.rotation += dt * ROTATION_SPEED
			self.x_speed += (32 * dt * ACCELERATION * math.cos(self.rotation))
			self.y_speed += (32 * dt * ACCELERATION * math.sin(self.rotation))
		if pyglet.window.key.RIGHT in presed_keys:
			self.rotation -= dt * ROTATION_SPEED
			self.x_speed += (32 * dt * ACCELERATION * math.cos(self.rotation))
			self.y_speed += (32 * dt * ACCELERATION * math.sin(self.rotation))
		if pyglet.window.key.SPACE in presed_keys and self.laser < 0:
			objects.append(Laser(self.x,self.y,self.x_speed,self.y_speed,self.rotation))
			self.laser = 0.9
		self.x = self.x + dt * self.x_speed
		self.y = self.y + dt * self.y_speed	
		self.sprite.rotation = 90 - math.degrees(self.rotation)
		self.sprite.x = self.x
		self.sprite.y = self.y
		self.laser -= dt

		for i in range(len(objects)):
			spaceship_radius = self.sprite.width // 2
			spaceship_x = self.x + spaceship_radius
			spaceship_y = self.y + spaceship_radius
			asteroid_radius = objects[i].sprite.width // 2
			asteroid_x = objects[i].x + asteroid_radius
			asteroid_y = objects[i].y + asteroid_radius
			if clash(asteroid_x,asteroid_y,spaceship_x,spaceship_y,asteroid_radius,spaceship_radius) and objects[i].__str__() == "Asteroid":
				objects[i] = Asteroid("random")
				lives.promena -= 1
				self.__init__()
	def draw(self):
		self.sprite.draw()
class Asteroid:
	def __init__(self,file):
		if file == "random":
			files = ["meteorBrown_big2.png","meteorGrey_big2.png","meteorBrown_big4.png","meteorGrey_big4.png","meteorBrown_big1.png","meteorGrey_big1.png","meteorBrown_big3.png","meteorGrey_big3.png","meteorBrown_med1.png","meteorGrey_med1.png","meteorBrown_med3.png","meteorGrey_med2.png","meteorBrown_small1.png","meteorGrey_small1.png","meteorBrown_small2.png","meteorGrey_small2.png","meteorGrey_tiny1.png","meteorBrown_tiny1.png","meteorGrey_tiny2.png","meteorBrown_tiny2.png"]
			file = random.choice(files)
		path = "images\\PNG\\Meteors\\"
		self.file = file
		image = pyglet.image.load(path + file)
		image.anchor_x = image.width // 2
		image.anchor_y = image.height // 2
		self.sprite = pyglet.sprite.Sprite(image)
		self.x = random.randrange(image.width,window.width - image.width)
		self.y = random.randrange(image.height,window.height - image.height)
		self.x_speed = random.randrange(0,11)
		self.y_speed = random.randrange(0,11)
		self.rotation = random.randrange(int(2 * math.pi))
		self.sprite.x = self.x
		self.sprite.y = self.y
		self.sprite.rotation = 90 - math.degrees(self.rotation)
	def tick(self,dt):
		direction = random.choice(["UP","DOWN","LEFT","RIGHT"])
		if "UP" == direction:
			self.x_speed += dt * ACCELERATION * math.cos(self.rotation) // 20
			self.y_speed += dt * ACCELERATION * math.sin(self.rotation) // 20
		if "DOWN" == direction:
			self.x_speed -= dt * ACCELERATION * math.cos(self.rotation) // 20
			self.y_speed -= dt * ACCELERATION * math.sin(self.rotation) // 20
		if "LEFT" == direction:
			self.rotation += dt * ROTATION_SPEED
			self.x_speed += (32 * dt * ACCELERATION * math.cos(self.rotation)) // 20
			self.y_speed += (32 * dt * ACCELERATION * math.sin(self.rotation)) // 20
		if "RIGHT" == direction:
			self.rotation -= dt * ROTATION_SPEED
			self.x_speed += (32 * dt * ACCELERATION * math.cos(self.rotation)) // 20
			self.y_speed += (32 * dt * ACCELERATION * math.sin(self.rotation)) // 20
		self.x = self.x + dt * self.x_speed
		self.y = self.y + dt * self.y_speed	
		self.sprite.rotation = 90 - math.degrees(self.rotation)
		self.sprite.x = self.x
		self.sprite.y = self.y
		if self.y > window.width or self.y > window.height or self.y < 0 or self.x < 0:
			self.__init__("random")
	def draw(self):
		self.sprite.draw()
	def __str__(self):
		return "Asteroid"
class Laser:
	def __init__(self,x,y,x_speed,y_speed,rotation):
		self.x = x
		self.y = y
		self.rotation = rotation
		if x_speed > 0:
			self.x_speed = x_speed + 100
		if y_speed > 0:
			self.y_speed = y_speed + 100
		if x_speed < 0:
			self.x_speed = x_speed - 100
		if y_speed < 0:
			self.y_speed = y_speed - 100
		if x_speed == 0:
			self.x_speed = ACCELERATION * math.cos(self.rotation)
		if y_speed == 0:
			self.y_speed = ACCELERATION * math.sin(self.rotation)
		self.sprite = pyglet.sprite.Sprite(pyglet.image.load("images\\PNG\\Lasers\\laserRed16.png"))
		self.sprite.x = self.x
		self.sprite.y = self.y
		self.sprite.rotation = 90 - math.degrees(self.rotation)
	def tick(self,dt):
		self.x += dt * self.x_speed
		self.y += dt * self.y_speed
		self.sprite.x = self.x
		self.sprite.y = self.y
		for i in range(len(objects)):
			spaceship_radius = self.sprite.width // 2
			spaceship_x = self.x + spaceship_radius
			spaceship_y = self.y + spaceship_radius
			asteroid_radius = objects[i].sprite.width // 2
			asteroid_x = objects[i].x + asteroid_radius
			asteroid_y = objects[i].y + asteroid_radius
			if clash(asteroid_x,asteroid_y,spaceship_x,spaceship_y,asteroid_radius,spaceship_radius) and objects[i].__str__() == "Asteroid":
				file = objects[i].file[6:-4]
				number = int(file[-1])
				file = file[0:-1]
				color = file[0:file.find("_")]
				file = file[len(color):-1] + file[-1]
				category = file[1:-1] + file[-1]
				if number == 3:
					number = 1
				if number == 4:
					number = 2

				categorys = ["tiny","small","med","big"]
				if category != "tiny":
					category = categorys[categorys.index(category) - 1]
					puvodni = objects[i]
					objects[i] = Asteroid("meteor" + color + "_" + category + str(number) + ".png")
					objects[i].x = puvodni.x
					objects[i].y = puvodni.y
					objects[i].rotation = puvodni.rotation
					objects[i].x_speed = dt * ACCELERATION * math.cos(objects[i].rotation)
					objects[i].y_speed = dt * ACCELERATION * math.sin(objects[i].rotation)
					objects.append(Asteroid("meteor" + color + "_" + category + str(number) + ".png"))
					objects[-1].x = puvodni.x
					objects[-1].y = puvodni.y
					objects[-1].rotation = puvodni.rotation
					objects[-1].x_speed = dt * ACCELERATION * math.cos(objects[-1].rotation)
					objects[-1].y_speed = dt * ACCELERATION * math.sin(objects[-1].rotation)
				else:
					objects[i] = Asteroid("blank.png")

def call_tick(dt):
	if lives.promena >= 0:
		for i in objects:
			i.tick(dt)
	else:
		window.clear()
		GameOver().draw()
def clash(asteroid_x,asteroid_y,spaceship_x,spaceship_y,asteroid_radius,spaceship_radius):
	if asteroid_x > spaceship_x:
		x = asteroid_x - spaceship_x
	else:
		x = spaceship_x - asteroid_x
	if asteroid_y > spaceship_y:
		y = asteroid_y - spaceship_y
	else:
		y = spaceship_y - asteroid_y
	if x > y:
		if x < (asteroid_radius + spaceship_radius):
			return True
		else:
			return False
	else:
		if y < (asteroid_radius + spaceship_radius):
			return True
		else:
			return False

objects = [Spaceship(),Asteroid("random"),Asteroid("random"),Asteroid("random"),Asteroid("random")]


@window.event
def on_draw():
	window.clear()
	if lives.promena >= 0:
		if lives.promena <= 9:
			numbers[lives.promena].draw()
		else:
			numbers[9].draw()
		for i in objects:
			i.sprite.draw()
		x = pyglet.sprite.Sprite(pyglet.image.load("images\\PNG\\UI\\numeralX.png"))
		life = pyglet.sprite.Sprite(pyglet.image.load("images\\PNG\\UI\\playerLife1_blue.png"))
		x.y = window.height - 60
		life.y = window.height - 60
		x.x = 50
		life.x = 100
		x.scale = 2
		life.scale = 2
		x.draw()
		life.draw()
	else:
		gameover = GameOver()
		gameover.sprite.y = window.height // 3
		gameover.sprite.x = window.width // 3
		gameover.draw()


@window.event
def on_key_press(key_code,modifier):
	if key_code == pyglet.window.key.UP or key_code == pyglet.window.key.LEFT or key_code == pyglet.window.key.RIGHT or key_code == pyglet.window.key.DOWN or key_code == pyglet.window.key.SPACE:
		presed_keys.append(key_code)
	if key_code == pyglet.window.key.R:
		objects[0] = Spaceship()
		lives.promena = 9
	if key_code == pyglet.window.key.ENTER:
		if not window.fullscreen:
			window = pyglet.window.Window(fullscreen = True)
		else:
			window = pyglet.window.Window(fullscreen = False)
@window.event
def on_key_release(key_code,modifier):
	if key_code in presed_keys:
		del presed_keys[presed_keys.index(key_code)]

lives = globalni()
lives.promena = 9
pyglet.clock.schedule_interval(call_tick,1/30)
pyglet.app.run()