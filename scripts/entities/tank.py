import pygame

from scripts.sprite_manager import SpriteManager

class Tank:

    def __init__(self, pos_x: int, pos_y: int) -> None:
        """
        initialisiert den Tank und setzt ihn an die Positionen pos_x und pos_y
        Arguments:
            pos_x (int): die x-Koordinate für die linke obere Ecke
            pos_y (int): die y-Koordinate für die linke obere Ecke
        """
        self.sprite_manager: SpriteManager = SpriteManager()

        self.tank: pygame.Surface = self.sprite_manager.load_sprite("assets/Tank.png", (90, 90))
        self.tank_dimensions: int = 90

        self.pos: list = [pos_x, pos_y]
        
        self.rect: pygame.Rect = self.tank.get_rect()
        self.rect.topleft = self.pos

        self.overheatbar: pygame.Rect = pygame.Rect(self.pos[0] - 10, self.pos[1], 10, self.tank_dimensions)

        self.hp = 100 # Prozent
        #self.healthbar: pygame.Rect = pygame.Rect(self.pos[0], self.pos[1] + self.tank_dimensions + 5, self.tank_dimensions * self.hp / 100, 10)

    
    def draw_tank(self, screen: pygame.Surface) -> None:
        """ 
        rendert den Tank an das gegebene Surface
        Arguments:
            screen (pygame.Surface): surface, auf das gerendert werden soll
        """
        screen.blit(self.tank, (self.pos[0], self.pos[1]))
        pygame.draw.rect(screen, "blue", self.overheatbar)
        self.healthbar: pygame.Rect = pygame.Rect(self.pos[0], self.pos[1] + self.tank_dimensions + 5, self.tank_dimensions * self.hp / 100, 10)
        pygame.draw.rect(screen, "red", self.healthbar)

    
    def update(self, keys: list, screen_width: int) -> None:
        """
        updated die x-Koordinaten des Tanks bei Tastendruck von rechter und linker Pfeiltaste oder A und D
        Arguments:
            keys (list): z.B. pygame.key.get_pressed()
            screen_width (int): Breite des Fensters
        """
        # Tank bewegen
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.pos[0] += 12
            self.overheatbar.x = self.pos[0] - 10
            self.healthbar.x = self.pos[0]
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.pos[0] -= 12
            self.overheatbar.x = self.pos[0] - 10
            self.healthbar.x = self.pos[0]

        # screen wrapping
        if self.pos[0] + self.tank.get_width() < 0:
            self.pos[0] = screen_width
        if self.pos[0] > screen_width:
            self.pos[0] = -self.tank.get_width()

        # Updaten vom collisionsrect
        self.rect.topleft = self.pos