import pygame
from random import randint

from scripts.sprite_manager import SpriteManager

class Meteor:

    # blockiert das rendern von schwarzer Farbe, damit Hitergrund vom Sprite transparent erscheint
    COLORKEY: tuple = (0, 0, 0)
    # Liste erstellen, damit alle Meteoriten gerendert werden können statt nur einer
    meteor_array: list = []

    def __init__(self, pos_x: int, pos_y: int, game) -> None:
        self.game = game

        self.sprite_manager: SpriteManager = SpriteManager()

        self.meteor: pygame.Surface = self.sprite_manager.load_sprite("assets/Meteorit.png", (100, 100))
        self.meteor.set_colorkey(self.COLORKEY)
        self.meteor_dimensions: int = 100

        self.pos: list = [pos_x, pos_y]
        self.rect: pygame.Rect = pygame.Rect(self.meteor.get_rect())
        self.rect.topleft = self.pos

    
    def set_position(self) -> int:
        x: int = randint(0, self.game.screen_size[0] - self.meteor_dimensions)
        return x
    

    def add(self) -> None:
        self.meteor_array.append(Meteor(self.set_position(), 0, self.game))


    def update_position(self) -> None:
        self.pos[1] += 5
        self.rect.y = self.pos[1]

    
    def draw_meteor(self, screen: pygame.Surface) -> None:
        for i, object in enumerate(self.meteor_array[:]):
            screen.blit(self.meteor, (object.pos[0], object.pos[1]))
            object.update_position()
            if object.pos[1] > self.game.screen_size[1] - self.meteor_dimensions:
                self.meteor_array.pop(i)