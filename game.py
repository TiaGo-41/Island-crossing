import pygame
import pytmx
import pyscroll



class Game:

    def __init__(self):
        #creer la fenetre
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("island crossing")

        #charger la carte (tmx)
        tmx_data = pytmx.util_pygame.load_pygame('carte1.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1.5

        #generer le joueur
        self.player = Player()

        #dessiner les calques
        self.groupe = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.groupe.add(self.player)

    def run(self):

        # boucle
        running = True

        while running:

            self.groupe.draw(self.screen)
            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()