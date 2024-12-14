import pygame

from scripts.sprite_manager import SpriteManager

class Menu:

    def __init__(self, game: object) -> None:
        self.game: object = game
        self.sprite_manager: SpriteManager = SpriteManager()

        # Positionen der Buttons
        self.start_button_pos: tuple = (100, 100)
        self.tutorial_button_pos: tuple = (100, 200)
        self.quit_button_pos: tuple = (100, 300)

        # Buttons initialisieren
        self.start_button: pygame.Surface = self.sprite_manager.load_sprite("assets/ui/Start_Button.png", (160, 80))
        self.start_button_rect: pygame.Rect = pygame.Rect(
            self.start_button_pos[0], self.start_button_pos[1], self.start_button.get_width(), self.start_button.get_height())
        self.start_button_hover: pygame.Surface = self.sprite_manager.load_sprite("assets/ui/Start_Button_Hover.png", (160, 80))

        self.quit_button: pygame.Surface = self.sprite_manager.load_sprite("assets/ui/Quit_Button.png", (160, 80))
        self.quit_button_rect: pygame.Rect = pygame.Rect(
            self.quit_button_pos[0], self.quit_button_pos[1], self.quit_button.get_width(), self.quit_button.get_height())
        self.quit_button_hover: pygame.Surface = self.sprite_manager.load_sprite("assets/ui/Quit_Button_Hover.png", (160, 80))

        self.tutorial_button: pygame.Surface = self.sprite_manager.load_sprite("assets/ui/Tutorial_Button.png", (220, 80))
        self.tutorial_button_rect: pygame.Rect = pygame.Rect(
            self.tutorial_button_pos[0], self.tutorial_button_pos[1], self.tutorial_button.get_width(), self.tutorial_button.get_height())
        self.tutorial_button_hover: pygame.Surface = self.sprite_manager.load_sprite(
            "assets/ui/Tutorial_Button_Hover.png", (220, 80))


    def load_main_menu(self, screen: pygame.Surface) -> None:
        screen.fill(self.game.COLOR_BACKGROUND)
        # Start Button
        if self.start_button_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(self.start_button_hover, self.start_button_pos)
        else:
            screen.blit(self.start_button, self.start_button_pos)
        
        # Tutorial Button
        if self.tutorial_button_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(self.tutorial_button_hover, self.tutorial_button_pos)
        else:
            screen.blit(self.tutorial_button, self.tutorial_button_pos)
        
        # Quit Button
        if self.quit_button_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(self.quit_button_hover, self.quit_button_pos)
        else:
            screen.blit(self.quit_button, self.quit_button_pos)
        pygame.display.update()