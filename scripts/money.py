import pygame

class Money:

    # Farbe für den Punktestandtext im Hintergrund (hellgrau)
    COLOR_SCORE: tuple = (125, 125, 120)

    def __init__(self) -> None:
        """ beinhaltet das derzeitige Geld des Spielers, initialisiert mit dem Geld auf 0 und einer fonr size von 350 """
        self.coins = 0
        self.font = pygame.font.Font(None, 350)
        self.coin_text = None
        self.update_coin_text()

    
    def update_coin_text(self) -> None:
        """ updated den Text des Geldes und setzt die Alpha auf 125 (ungefähr Hälfte) """
        self.coin_text = self.font.render(f"{self.coins}", True, self.COLOR_SCORE).convert()
        self.coin_text.set_alpha(125)


    def add_money(self, amount: int) -> None:
        """
        fügt dem Geldspeicher die angegebene Menge hinzu
        Arguments:
            amount (int): die Menge, die hinzugefügt werden soll
        """
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