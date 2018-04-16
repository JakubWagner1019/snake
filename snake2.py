#_snake2

import pygame
import random

displayWidth=800
displayHeight=600

distance=50
gap=distance-40
rect = lambda x,y: [x[0],x[1],y[0],y[1]]
add = lambda x,y: (x[0]+y[0],x[1]+y[1])

white=(255,255,255)
black=(0,0,0)

gameSpeed = 1

class Map:
	def __init__(self):
		self.position=(100,100)
		self.size=8
		self.length=(gap+self.size*distance,gap+self.size*distance)
		self.start=add(self.position,(gap,gap))
		self.center=add(self.start,(distance*self.size/2,distance*self.size/2))
	def draw(self,gameDisplay):
		pygame.draw.rect(gameDisplay,black,rect(self.position,self.length))
	def getRandom(self):
		return add(self.start,(distance*random.randint(0,self.size-1),distance*random.randint(0,self.size-1)))
	def isOutside(self,pos):
		self.ends=add(self.position,self.length)
		if pos[0]<self.start[0] or pos[0]>=self.ends[0]:
			return True
		if pos[1]<self.start[1] or pos[1]>=self.ends[1]:
			return True
	
class Block:
	def __init__(self,img,pos):
		self.position=pos
		self.img=img
	def draw(self,gameDisplay):
		gameDisplay.blit(self.img,self.position)
	
class Snake:
	def __init__(self,img,pos):
		self.alive=True
		self.satisfied=False
		self.direction=(0,0)
		self.blocks=[]
		self.img=img
		for i in range(0,3):
			self.blocks.append(Block(img,add(pos,(distance*i,0))))
	def draw(self,gameDisplay):
		for block in self.blocks:
			block.draw(gameDisplay)
	def move(self,map,apple):
		if self.direction!=(0,0):
			newBlock=Block(self.img,add(self.blocks[0].position,self.direction))
			for block in self.blocks:
				if newBlock.position==block.position:
					snake.alive=False
			if map.isOutside(newBlock.position):
				snake.alive=False
			if newBlock.position==apple.position:
				self.satisfied=True
				apple.position=map.getRandom()
			if snake.alive:
				if self.satisfied:
					self.blocks=[newBlock]+self.blocks
					self.satisfied=False
				else:
					self.blocks=[newBlock]+self.blocks[0:-1]
	
pygame.init()

gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
pygame.display.set_caption('Snake2')
clock = pygame.time.Clock()

img_snake = pygame.image.load('img_snake.png')
img_apple = pygame.image.load('img_apple.png')

map = Map()
snake = Snake(img_snake,map.center)
apple = Block(img_apple,map.getRandom())

i=0
quitting = False
while not quitting:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quitting = True
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				quitting = True
			if event.key == pygame.K_UP:
				snake.direction = (0,-distance)
			if event.key == pygame.K_DOWN:
				snake.direction = (0,distance)
			if event.key == pygame.K_LEFT:
				snake.direction = (-distance,0)
			if event.key == pygame.K_RIGHT:
				snake.direction = (distance,0)
	
	if snake.alive:
		i+=0.1
		if i>(1.0/gameSpeed):
			snake.move(map,apple)
			i=0
			
	gameDisplay.fill(white)
	map.draw(gameDisplay)
	snake.draw(gameDisplay)
	apple.draw(gameDisplay)
	pygame.display.update()
	clock.tick(60)
	
pygame.quit()
quit()