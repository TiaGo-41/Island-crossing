import pygame


class Player(pygame.sprite.Sprite) :

    def __init__(self):
        super().__init__()
        self.sprite_sheet = pygame.image.load('resources\Modern tiles_Free\Characters_free\Adam_16x16.png')
        self.image = sel.get_image(0, 0)
        self.rect = self.image.get_rect()

    def get_image(self, x, y):
        image = pygame.Surface([16, 16])
        image.blit(self.sprite_sheet, (0, 0), (x, y, 16,  16))
        return image