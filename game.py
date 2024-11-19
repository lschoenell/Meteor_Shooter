import sys
import pygame
from ammo import Ammo
from meteor import Meteor
from random import randint

class Game:

    COLOR_BACKGROUND = (85, 85, 85) # Farbe vom Hintergrund (dunkelgrau)
    COLOR_SCORE = (125, 125, 120) # Farbe vom Score auf dem Hintergrund (hellgrau)
    COLORKEY = (0, 0, 0)
    score = 0

    print("Deine Mutter ist ein Meteorit")

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Meteor Shooter of Absolute Doom")

        # Screen initialisieren
        self.screen_size = (1000, 700)
        self.screen_middle = (self.screen_size[0] / 2, self.screen_size[1] / 2)
        self.screen = pygame.display.set_mode(self.screen_size)

        # Gameclock für fps
        self.clock = pygame.time.Clock()

        # Tank initialisieren und hoch scalen
        self.tank = pygame.image.load("assets/Tank.png").convert()
        self.tank.set_colorkey(self.COLORKEY)
        self.tank = pygame.transform.scale(self.tank, (90, 90)) # transformiert Tank zu 90 width und height
        self.tank_dimensions = 90

        # Startposition des Tanks setzen
        self.tank_pos = [self.screen_middle[0] - (self.tank_dimensions / 2), self.screen_size[1] - (self.tank_dimensions + 10)]

        # Rect für collisions des Tanks
        self.tank_rect: pygame.Rect = pygame.Rect(self.tank_pos[0], self.tank_pos[1], self.tank_dimensions, self.tank_dimensions)

        # Ammo initialisieren und hoch scalen
        self.ammo: pygame.Surface = pygame.image.load("assets/Ammo.png").convert()
        self.ammo.set_colorkey(self.COLORKEY)
        self.ammo = pygame.transform.scale(self.ammo, (55, 55))
        self.ammo_dimensions: int = 55
        self.ammo_array: list  = []

        # Meteor initialisieren und hoch scalen
        self.meteor = pygame.image.load("assets/Meteorit.png").convert()
        self.meteor.set_colorkey(self.COLORKEY)
        self.meteor = pygame.transform.scale(self.meteor, (100, 100))
        self.meteor_dimensions: int = 100
        self.meteor_array: list = []

    
    # Tank auf screen setzen
    def draw_tank(self) -> None:
        self.screen.blit(self.tank, self.tank_pos)


    # Tank bewegen und wrappen
    def move_tank(self) -> None:
        # inputhandler für den Tank
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.tank_pos[0] += 12
        if keys[pygame.K_LEFT]:
            self.tank_pos[0] -= 12

        # screen wrapping für den Tank
        if self.tank_pos[0] + self.tank_dimensions < 0:
            self.tank_pos[0] = self.screen_size[0]
        if self.tank_pos[0] > self.screen_size[0]:
            self.tank_pos[0] = -self.tank_dimensions


    def shoot_ammo(self) -> None:
        # alle Schüsse im array auf dem screen laden und hochfliegen lassen
        for i, object in enumerate(self.ammo_array):
            self.screen.blit(self.ammo, (object.pos_x, object.pos_y))
            object.pos_y -= 13
            object.rect.y = object.pos_y
            # wenn die Kugeln außerhalb des Bildschirms sind, werden sie gelöscht
            # (oder wenn sie auf Meteor treffen)
            if object.pos_y < 0 - self.ammo_dimensions:
                self.ammo_array.pop(i)


    def set_meteor_pos(self) -> int:
        pos_x = randint(0, self.screen_size[0] - self.meteor_dimensions)
        return pos_x


    def draw_meteor(self) -> None:
        for i, object in enumerate(self.meteor_array):
            self.screen.blit(self.meteor, (object.pos_x, object.pos_y))
            object.pos_y += 5
            object.rect.y = object.pos_y
            if object.pos_y > self.screen_size[1] - self.meteor_dimensions:
                self.meteor_array.pop(i)
                

    # Zeigt den aktuellen Score in der Mitte
    def show_score(self) -> None:
        font = pygame.font.Font(None, 350)
        score_text = font.render(f"{self.score}", True, self.COLOR_SCORE).convert()
        score_text.set_alpha(125)
        self.screen.blit(score_text, (self.screen_middle[0] - (score_text.get_width() / 2), self.screen_middle[1] - (score_text.get_height() / 2 )))     


    # eventhandler
    def handle_events(self) -> None:
        for event in pygame.event.get():
            # Fenster schließen
            if event.type == pygame.QUIT: # nur event gibt <Event(256-Quit {})> wieder, event.type ein int
                pygame.quit()
                sys.exit()

            # Leertaste gibt neues Ammo Object ins Muni-array
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.ammo_array.append(Ammo(self.tank_pos[0] + (self.tank_dimensions / 2) - (self.ammo_dimensions / 2), self.tank_pos[1] - (self.ammo_dimensions - 15)))

                    
        # Keyhandling für tank und Positionen updaten
        self.move_tank()


    def handle_collisions(self) -> None:
        for ammo in self.ammo_array[:]:
            for meteor in self.meteor_array[:]:
                if ammo.rect.colliderect(meteor.rect):
                    self.ammo_array.remove(ammo)
                    self.meteor_array.remove(meteor)
                    self.score += 1
                    break


    # gameloop: wird 60 mal pro Sekunde ausgeführt
    def run(self) -> None:
        start = pygame.time.get_ticks()
        while True:
            self.handle_events()
            self.screen.fill(self.COLOR_BACKGROUND) # !!! WICHTIG DAMIT ALTEN FRAMES GELÖSCHT WERDEN !!!
            self.show_score()
            now = pygame.time.get_ticks()
            if now - start > 1000:
                start = now
                self.meteor_array.append(Meteor(self.set_meteor_pos(), 0))
            self.draw_meteor()
            self.draw_tank()
            self.shoot_ammo()
            self.handle_collisions()
            pygame.display.update()
            self.clock.tick(60)

Game().run()