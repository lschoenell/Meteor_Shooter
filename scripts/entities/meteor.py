import pygame
from random import randint

from scripts.sprite_manager import SpriteManager

class Meteor:

    # Liste erstellen, damit alle Meteoriten gerendert werden können statt nur einer
    meteor_array: list = []

    def __init__(self, pos_x: int, pos_y: int, game: object) -> None:
        """
        Initialisiert ein einzelnes Meteor-Objekt and den gegebenen Positionen
        Arguments: 
            pos_x (int): die x-Koordinate für die linke obere Ecke
            pos_y (int): die y-Koordinate für die linke obere Ecke
            game (object): die main Klasse zur Handhabung von Interaktionen zwischen den Klassen
        """
        self.game = game

        self.sprite_manager: SpriteManager = SpriteManager()

        self.meteor: pygame.Surface = self.sprite_manager.load_sprite("assets/Meteorit.png", (100, 100))
        self.meteor_dimensions: int = 100

        self.pos: list = [pos_x, pos_y]
        self.rect: pygame.Rect = pygame.Rect(self.meteor.get_rect())
        self.rect.topleft = self.pos

    
    def set_position(self) -> int:
        """ 
        setzt eine zufällige Zahl zwischen 0 und der Breite des Fensters als x-Koordinate des Meteorits
        Returns:
            x (int): die generierte x-Koordinate 
        """
        x: int = randint(0, self.game.screen_size[0] - self.meteor_dimensions)
        return x
    

    def add(self) -> None:
        """ fügt dem internen meteor-array ein neues Objekt an zufälliger x-Position hinzu """
        self.meteor_array.append(Meteor(self.set_position(), 0 - self.meteor_dimensions, self.game))


    def update_position(self) -> None:
        """ updated die y-Koordinate des Meteors und des collisionrects nach unten """
        self.pos[1] += 5
        self.rect.y = self.pos[1]

    
    def draw_meteor(self, screen: pygame.Surface) -> None:
        """
        iteriert über das interne meteor-array und rendert jedes einzelne Meteor-Objekt daraus. Updated in jedem Schritt die y-Positionen, sodass der Meteor nach unten fliegt
        Arguments:
            screen (pygame.Surface): das Surface, auf das gerendert werden soll
        """
        for i, object in enumerate(self.meteor_array[:]):
            screen.blit(self.meteor, (object.pos[0], object.pos[1]))
            object.update_position()