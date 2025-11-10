import pygame
from scripts.sprite_manager import SpriteManager

class Power_Ups:

    COST: int = 800
    SIZE: tuple = (90, 90)

    def __init__(self, game: object) -> None:
        """ initialisiert die Power-Up-Klasse, die zugehoerigen Sprites und die Kollisionsrechtecke der Power-Ups """
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

        # Font fuer Beschreibungen
        self.font: pygame.font.Font = pygame.font.Font(None, 24)
        
        # Beschreibungstexte erstellen
        self.speed_desc_lines = [
            f"Cost: {self.COST}",
            "gives the tank 15% more speed"
        ]
        self.cooling_desc_lines = [
            f"Cost: {self.COST}",
            "gives the tank 10% more overheat cooling"
        ]
        
        # Render die Beschreibungen
        self.speed_desc_surfs = [self.font.render(line, True, (200, 200, 200)) for line in self.speed_desc_lines]
        self.cooling_desc_surfs = [self.font.render(line, True, (200, 200, 200)) for line in self.cooling_desc_lines]

    
    def apply_powerup(self, type: str) -> None:
        """
        updated die Werte des Tanks basierend auf dem uebergebenen Typs

        Arguments:
        ---------
            type (str): "speed" oder "cooling"
        """
        if type == "speed":
            self.game.tank.move_speed *= 1.15 # erhoeht um 15%
        elif type == "cooling":
            self.game.tank.cooling_value *= 1.1 # erhoeht um 10%

    
    def draw(self, screen: pygame.Surface) -> None:
        """
        rendert die Power-Ups auf das angegebene Surface und handhabt die Logik der Beschreibungen

        Arguments:
        ---------
            screen (pygame.Surface): Surface, auf das gerendert werden soll
        """

        # Powerups zeichnen
        screen.blit(self.speed_powerup, self.speed_powerup_pos)
        screen.blit(self.cooling_powerup, (self.cooling_powerup_pos))
        
        # Mausposition pruefen
        mouse_pos = pygame.mouse.get_pos()
        
        # Position fuer die Beschreibungen in der Mitte des Bildschirms
        desc_x = self.game.screen_size[0] / 2
        desc_y = 200  # Ueber dem Geld-Counter
        
        # Beschreibung fuer Speed Powerup anzeigen wenn Maus darueber
        if self.speed_powerup_colrect.collidepoint(mouse_pos):
            y_offset = desc_y
            for surf in self.speed_desc_surfs:
                # Zentriere den Text horizontal
                x_pos = desc_x - (surf.get_width() / 2)
                screen.blit(surf, (x_pos, y_offset))
                y_offset += surf.get_height()
        
        # Beschreibung fuer Cooling Powerup anzeigen wenn Maus darueber
        if self.cooling_powerup_colrect.collidepoint(mouse_pos):
            y_offset = desc_y
            for surf in self.cooling_desc_surfs:
                # Zentriere den Text horizontal
                x_pos = desc_x - (surf.get_width() / 2)
                screen.blit(surf, (x_pos, y_offset))
                y_offset += surf.get_height()
