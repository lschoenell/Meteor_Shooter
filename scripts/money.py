import pygame

class Money:

    # Farbe für den Punktestandtext im Hintergrund (hellgrau)
    COLOR_SCORE: tuple = (125, 125, 120)

    def __init__(self) -> None:
        """ beinhaltet das derzeitige Geld des Spielers, initialisiert mit dem Geld auf 0  """
        self.coins: int = 0
        self.font: pygame.font.Font = pygame.font.Font(None, 350)
        self.coin_text: pygame.Surface = None
        self.update_coin_text()

    
    def update_coin_text(self) -> None:
        """ updated den Text des Geldes und setzt die Alpha auf 125 (ungefähr Hälfte) """
        self.coin_text = self.font.render(f"{self.coins}", True, self.COLOR_SCORE).convert_alpha()
        self.coin_text.set_alpha(125)


    def add_money(self, amount: int) -> None:
        """
        fügt dem Geldspeicher die angegebene Menge hinzu, egal ob positiv oder negativ und begrenzt die Untergrenze bei 0
        Arguments:
            amount (int): die Menge, die hinzugefügt werden soll
        """
        if amount < 0 and abs(amount) > self.coins:
            self.coins = 0
        else:
            self.coins += amount
        self.update_coin_text()


    def show_money(self, screen: pygame.Surface, screen_middle_x: int, screen_middle_y: int) -> None:
        """ 
        rendert das Geld auf das angegebene Surface an den gegebenen Koordinaten
        Arguments:
            screen (pygame.Surface): Surface, auf das gerendert werden soll
            screen_middle_x (int): x-Koordinate, an die gerendert werden soll (hier die Fenstermitte) 
            screen_middle_y (int): y-Koordinate, an die gerendert werden soll (hier die Fenstermitte)
        """
        screen.blit(self.coin_text, (screen_middle_x - (self.coin_text.get_width() / 2), screen_middle_y - (self.coin_text.get_height() / 2 )))