import pygame

from scripts.sprite_manager import SpriteManager

class Ammo:

    # blockiert das rendern von schwarzer Farbe, damit Hitergrund vom Sprite transparent erscheint
    COLORKEY: tuple = (0, 0, 0)
    # offset, da das eigentliche Sprite nicht die obere Spitze da hat, wo das Bild tatsächlich oben endet
    sprite_offset_y: int = 26
    # Liste erstellen, damit alle geschossenen Schüsse gerendert werden können statt nur einer
    ammo_array: list = []

    def __init__(self, pos_x: int, pos_y: int, game: object) -> None:
        """
        Initialisiert eine einzelne Ammo an den gegebenen Positionen x und y
        Arguments:
            pos_x (int): die x-Koordinate für die linke obere Ecke
            pos_y (int): die y-Koordinate für die linke obere Ecke
            game (object): die main Klasse zur Handhabung von Interaktionen zwischen den Klassen
        """
        #self.ammo: pygame.Surface = pygame.image.load("assets/Ammo.png").convert()
        #self.ammo: pygame.Surface = pygame.transform.scale(self.ammo, (55, 55))
        self.sprite_manager: SpriteManager = SpriteManager()

        self.ammo: pygame.Surface = self.sprite_manager.load_sprite("assets/Ammo.png", (55, 55))
        self.ammo.set_colorkey(self.COLORKEY)
        self.ammo_dimensons: int = 55

        self.pos: list = [pos_x, pos_y]
        self.rect: pygame.Rect = self.ammo.get_rect()
        self.rect.topleft = [self.pos[0], self.pos[1] + self.sprite_offset_y]

        self.game = game

    
    def update(self) -> None:
        """
        Updated die y-Position der Ammo so, dass sie nach oben schießt und updated auch die Position des collisionrects
        """
        self.pos[1] -= 13
        self.rect.y = self.pos[1] + self.sprite_offset_y

    
    def add_ammo(self) -> None:
        """
        fügt dem ammo array ein Ammo Objekt an der Position des Rohrs des Panzers zu
        """
        self.ammo_array.append(Ammo(self.game.tank.pos[0] + (self.game.tank.tank_dimensions / 2) - (self.game.ammo.ammo_dimensons / 2), self.game.tank.pos[1] - (self.game.ammo.ammo_dimensons - 15), self.game))


    def draw_ammo(self, screen: pygame.Surface) -> None:
        """
        rendert alle Objekte des ammo arrays auf den gegebenen screen und löscht alle Ammo Objekte, die außerhalb des Bildschirms fliegen
        Arguments:
            screen (pygame.Surface): Surface, auf das gerendert werden soll
        """
        # slicing ([:]) auf das ammo_array, damit durch eine interne Kopie iteriert wird, die nicht dynamisch veraendert werden kann, damit eventuelle Indexprobleme bei pop() behoben werden
        for i, object in enumerate(self.ammo_array[:]):
            screen.blit(object.ammo, (object.pos[0], object.pos[1]))
            object.update()
            if object.pos[1] < 0 - self.ammo_dimensons:
                self.ammo_array.pop(i)