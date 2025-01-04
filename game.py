import pygame

class Game:

    def __init__(self):
        #creer la fenetre
        pygame.display.set_mode((800,600))
        pygame.display.set_caption("island crossing")
    
    def run(self):

        # boucle
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()