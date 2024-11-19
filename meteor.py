import pygame

class Meteor:

    def __init__(self, pos_x, pos_y) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        # Rect für collisions, Breite und Höhe sind die meteor_dimensions (100)
        self.rect = pygame.Rect(pos_x, pos_y, 100, 100)