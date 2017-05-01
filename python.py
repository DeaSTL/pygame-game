import pygame_setup


class main(pygame_setup.setup_):
	def run(self):
		self.pygame.draw.rect(self.display,(100,100,100),(100,100,100,100),10)
main(500,500).start()