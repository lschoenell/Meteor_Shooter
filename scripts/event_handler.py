import sys
import pygame

class EventHandler:

    def __init__(self, game) -> None:
        self.game = game


    def key_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game.ammo.add_ammo()


    def handle_collisions(self) -> None:
        pass