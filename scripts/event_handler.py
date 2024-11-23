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


    def ammo_collisions(self) -> bool:
        """ 
        checkt für Kollisionen zwischen einer Ammo und allen Meteoriten
        Returns:
            bool: True wenn ein ammo ein meteor getroffen hat, sonst False
        """
        for ammo in self.game.ammo.ammo_array[:]:
            for meteor in self.game.meteor.meteor_array[:]:
                if ammo.rect.colliderect(meteor.rect):
                    self.game.ammo.ammo_array.remove(ammo)
                    self.game.meteor.meteor_array.remove(meteor)
                    return True
        return False