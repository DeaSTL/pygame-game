import pygame_setup

class eventHandler(pygame_setup.eventHandler):
	def onDown(self):
		print("Down")


class main(pygame_setup.setup_):
	def run(self):
		self.pygame.draw.rect(self.display,(100,100,100),(100,100,100,100),10)
		self.eventHandler.mainKeyHandler()
	
main(500,500).start()