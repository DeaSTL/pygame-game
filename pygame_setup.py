import pygame
import sys

#global variables

global frameRate
global screenWidth
global screenHeight

pygame_inst = pygame



class eventHandler:
	def __init__(self):
		global pygame_inst
		global screenWidth
		global screenHeight
		global display

		self.pygame = pygame
		self.display = display

		
	def closeOnExit(self):
		for event in self.pygame.event.get():
			if event.type == self.pygame.QUIT:
				sys.exit(0)
	def onResize(self):
		for event in self.pygame.event.get():
			if event.type == self.pygame.VIDEORESIZE:
				self.display = self.pygame.display.set_mode((event.w,event.h),self.pygame.RESIZABLE)
				screenWidth = event.w
				screenHeight = event.h
				display = self.display
	def onLeft(self):
		for event in self.pygame.event.get():
			if event.type == self.pygame.KEYDOWN:
				if event.key == self.pygame.K_LEFT  or self.python.K_a:
					return True
				else:
					return False
			else:
				return False
	def onRight(self):
		for event in self.pygame.event.get():
			if event.type == self.pygame.KEYDOWN:
				if event.key == self.pygame.K_RIGHT  or self.python.K_d:
					return True
				else:
					return False
			else:
				return False
	def onUp(self):
		for event in self.pygame.event.get():
			if event.type == self.pygame.KEYDOWN:
				if event.key == self.pygame.K_UP  or self.python.K_s:
					return True
				else:
					return False
			else:
				return False
	def onDown(self):
		for event in self.pygame.event.get():
			if event.type == self.pygame.KEYDOWN:
				if event.key == self.pygame.K_DOWN or self.python.K_s:
					return True
				else:
					return False
			else:
				return False
class draw:
	def __init__(self):
		pass
	def drawText(string,x,y,color):
		label = myfont.render(string, 1, color)
		disp.blit(label,(x,y))

class setup_(object):
	def __init__(self,width,height):
		#screen variables
		global frameRate 
		global screenWidth
		global screenHeight
		global pygame_inst
		global display

		frameRate = 24
		screenWidth = width
		screenHeight = height

		self.frameRate = frameRate


		self.pygame = pygame_inst
		self.pygame.init()
		display = self.pygame.display.set_mode((screenWidth,screenHeight),self.pygame.RESIZABLE)
		self.display = display
		self.pygame.display.init()

		self.clock = self.pygame.time.Clock()
		self.font = self.pygame.font.SysFont("monospace",30)

		self.eventHandler = eventHandler()
	def run(self):
		pass	
	def start(self):
		while(True):
			self.run()

			#Closes when exited
			self.eventHandler.closeOnExit()
			self.display = display

			self.clock.tick(self.frameRate)
			self.pygame.display.update()




