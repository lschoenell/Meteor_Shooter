import sys
import pygame

class EventHandler:

    def __init__(self, game: object) -> None:
        """
        Initialisiert den Event Handler
        Arguments:
            game (object): die game Instanz zum Zugriff auf alle Inhalte der game Logik
        """
        self.game: object = game


    def key_events(self) -> None:
        """ beinhaltet Handhabung der grundlegenden Eventtypen wie das Schließen des Fensters oder drücken von Tasten """
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # einzelner Tastendruck während des Spielens
            if event.type == pygame.KEYDOWN and self.game.game_state == self.game.PLAYING:
                if event.key == pygame.K_SPACE:
                    self.game.ammo.add_ammo()

            # einzelner Tastendruck während des Hauptmenüs
            if event.type == pygame.MOUSEBUTTONDOWN and self.game.game_state == self.game.MAIN_MENU:
                if mouse_x >= self.game.menu.start_button_pos[0] and mouse_x <= self.game.menu.start_button_pos[0] + self.game.menu.start_button.get_width():
                    x_inside = True
                
                if mouse_y >= self.game.menu.start_button_pos[1] and mouse_y <= self.game.menu.start_button_pos[1] + self.game.menu.start_button.get_height():
                    y_inside = True

                if x_inside and y_inside:                   
                    self.game.game_state = self.game.PLAYING


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