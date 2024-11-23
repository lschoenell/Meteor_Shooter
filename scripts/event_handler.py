import sys
import pygame

class EventHandler:

    def __init__(self, game: object) -> None:
        """
        Initialisiert den Event Handler
        Arguments:
            game (object): die game Instanz zum Zugriff auf alle Inhalte der game Logik
        """
        self.game = game


    def key_events(self) -> None:
        """ beinhaltet Handhabung der grundlegenden Eventtypen wie das Schließen des Fensters oder drücken von Tasten """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.game.ammo.add_ammo()


    def handle_ammo_collisions(self) -> None:
        pass