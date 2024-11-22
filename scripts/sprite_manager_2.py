import pygame

class SpriteManager:

    def __init__(self) -> None:
        self.sprites = {
            "assets/Ammo.png": pygame.transform.scale(
                pygame.image.load("assets/Ammo.png").convert(), (32, 32)
            ),
            "assets/Tank.png": pygame.transform.scale(
                pygame.image.load("assets/Tank.png").convert(), (64, 64)
            ),
            "assets/Meteorit.png": pygame.transform.scale(
                pygame.image.load("assets/Meteorit.png").convert(), (64, 64)
            ),
        }


    def get_sprite(self, path: str) -> None:
        return self.sprites[str]