import pygame
from scripts.sprite_manager import SpriteManager

class Power_Ups:

    COST: int = 800
    SIZE: tuple = (90, 90)

    def __init__(self, game: object) -> None:
        
        self.game: object = game
        self.sprite_manager: SpriteManager = SpriteManager()

        self.speed_powerup: pygame.Surface = self.sprite_manager.load_sprite("assets/powerups/Speed_Powerup.png", self.SIZE)
        self.speed_powerup_pos: tuple = (125, 125)
        self.speed_powerup_colrect: pygame.Rect = self.speed_powerup.get_rect()
        self.speed_powerup_colrect.topleft = self.speed_powerup_pos

        self.cooling_powerup: pygame.Surface = self.sprite_manager.load_sprite("assets/powerups/Cooling_Powerup.png", self.SIZE)
        self.cooling_powerup_pos: tuple = [self.game.screen_size[0] - (125 + self.SIZE[0]), 125]
        self.cooling_powerup_colrect: pygame.Rect = self.cooling_powerup.get_rect()
        self.cooling_powerup_colrect.topleft = self.cooling_powerup_pos

    
    def apply_powerup(self, type: str) -> None:

        if type == "speed":
            self.game.tank.move_speed *= 1.3 # erhoeht um 30%
        elif type == "cooling":
            self.game.tank.cooling_value *= 1.2 # erhoeht um 20%

    
    def draw(self, screen: pygame.Surface) -> None:
        
        screen.blit(self.speed_powerup, self.speed_powerup_pos)
        screen.blit(self.cooling_powerup, (self.cooling_powerup_pos))
