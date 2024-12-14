import pygame

from scripts.sprite_manager import SpriteManager

class Menu:

    def __init__(self, game: object) -> None:
        self.game: object = game
        self.sprite_manager: SpriteManager = SpriteManager()
        self.start_button: pygame.Surface = self.sprite_manager.load_sprite("assets/ui/Start_Button.png", (160, 80))
        self.quit_button: pygame.Surface = self.sprite_manager.load_sprite("assets/ui/Quit_Button.png", (160, 80))
        self.tutorial_button: pygame.Surface = self.sprite_manager.load_sprite("assets/ui/Tutorial_Button.png", (220, 80))


    def load_main_menu(self, screen: pygame.Surface) -> None:
        screen.fill(self.game.COLOR_BACKGROUND)
        screen.blit(self.start_button, (100, 100))
        screen.blit(self.tutorial_button, (100, 200))
        screen.blit(self.quit_button, (100, 300))
        pygame.display.update()