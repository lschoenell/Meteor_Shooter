import pygame

class Menu:

    def __init__(self, game: object) -> None:
        self.game = game

    
    def load_main_menu(self, screen: pygame.Surface) -> None:
        screen.fill(self.game.COLOR_BACKGROUND)
        pygame.display.update()