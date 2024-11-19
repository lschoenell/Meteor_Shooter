import pygame

class Ammo:
    
    def __init__(self, pos_x, pos_y) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        # Rect für collisions, Breite und Höhe sind die ammo_dimensions (55)
        self.rect = pygame.Rect(pos_x, pos_y, 55, 55)