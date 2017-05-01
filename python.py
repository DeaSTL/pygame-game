import pygame_setup

pygame_setup_instance = pygame_setup.setup_

eventHandler = pygame_setup_instance.eventHandler()
class main(pygame_setup_instance):
	def run(self):
		self.pygame.draw.rect(self.display,(100,100,100),(100,100,100,100),10)
class eventHandler(eventHandler):
	def onDown(self):
		print("down")
main(500,500).start()