import pygame

class Menu:

    def __init__(self, game: object) -> None:
        self.game = game
        self.font = pygame.font.Font(None, 200)
        self.start_button = self.font.render("Start", True, (255, 255, 255)).convert_alpha()
        self.start_button_positions = (self.game.screen_middle[0] - (self.start_button.get_width() / 2), self.game.screen_middle[1])

    
    def load_main_menu(self, screen: pygame.Surface) -> None:
        screen.fill(self.game.COLOR_BACKGROUND)
        screen.blit(self.start_button, (self.start_button_positions[0], self.start_button_positions[1]))
        pygame.display.update()