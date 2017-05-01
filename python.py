import pygame_setup



class main(pygame_setup.setup_):
	def run(self):
		self.pygame.draw.rect(self.display,(100,100,100),(100,100,100,100),10)
		if(self.eventHandler.onLeft()): print("left key")
main(500,500).start()