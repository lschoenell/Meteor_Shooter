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
        """ beinhaltet Handhabung der grundlegenden Eventtypen wie das Schliessen des Fensters oder druecken von Tasten """
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # einzelner Tastendruck waehrend des Spielens
            if event.type == pygame.KEYDOWN and self.game.game_state == self.game.PLAYING:
                if event.key == pygame.K_SPACE and not self.game.tank.is_overheated:
                    if self.game.tank.overheat_value < 100:
                        self.game.ammo.add_ammo()
                        new_overheat = min(100, self.game.tank.overheat_value + 25)
                        if new_overheat >= 100:
                            self.game.tank.is_overheated = True
                        self.game.tank.overheat_value = new_overheat

            # waehrend Power-Up Auswahl
            if event.type == pygame.MOUSEBUTTONDOWN and self.game.wave_system.wave_active == False:
                self.game.wave_system.wave_active = True

            # einzelner Maustastendruck im Hauptmenue
            if event.type == pygame.MOUSEBUTTONDOWN and self.game.game_state == self.game.MAIN_MENU:
                # Handling fuer den Play Button
                x_inside_play = False
                y_inside_play = False
                # Starten des Spiels beim druecken des Start Buttons
                if mouse_x >= self.game.menu.start_button_pos[0] and mouse_x <= self.game.menu.start_button_pos[0] + self.game.menu.start_button.get_width():
                    x_inside_play = True
    
                if mouse_y >= self.game.menu.start_button_pos[1] and mouse_y <= self.game.menu.start_button_pos[1] + self.game.menu.start_button.get_height():
                    y_inside_play = True

                if x_inside_play and y_inside_play:
                    self.game.game_state = self.game.PLAYING

                # Handling fuer den Quit Button
                x_inside_quit = False
                y_inside_quit = False
                # Schliessen des Spiels beim druecken des Quit Buttons
                if mouse_x >= self.game.menu.quit_button_pos[0] and mouse_x <= self.game.menu.quit_button_pos[0] + self.game.menu.quit_button.get_width():
                    x_inside_quit = True
                
                if mouse_y >= self.game.menu.quit_button_pos[1] and mouse_y <= self.game.menu.quit_button_pos[1] + self.game.menu.quit_button.get_width():
                    y_inside_quit = True

                if (x_inside_quit and y_inside_quit):
                    pygame.quit()
                    sys.exit()


    def collisions(self) -> bool:
        """ 
        checkt fuer Kollisionen zwischen einer Ammo und allen Meteoriten

        Returns:
        -------
            bool: True wenn ein ammo ein meteor getroffen hat, sonst False
        """
        for meteor in self.game.meteor.meteor_array[:]:
            for ammo in self.game.ammo.ammo_array[:]:
                if ammo.rect.colliderect(meteor.rect):
                    self.game.ammo.ammo_array.remove(ammo)
                    self.game.meteor.meteor_array.remove(meteor)
                    return True
            if meteor.rect.colliderect(self.game.tank.rect):
                self.game.tank.hp -= 50
                self.game.meteor.meteor_array.remove(meteor)
                self.game.money.add_money(-1000)
                if self.game.tank.hp <= 0:
                    self.game.game_state = self.game.MAIN_MENU
            if meteor.pos[1] > self.game.screen_size[1] - self.game.meteor.meteor_dimensions:
                self.game.meteor.meteor_array.remove(meteor)
                self.game.tank.hp -= 20
                self.game.money.add_money(-100)
                if self.game.tank.hp <= 0:
                    self.game.game_state = self.game.MAIN_MENU
        return False