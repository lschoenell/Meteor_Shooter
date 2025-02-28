import pygame

from scripts.entities.tank import Tank
from scripts.entities.ammo import Ammo
from scripts.entities.meteor import Meteor
from scripts.game_logic.event_handler import EventHandler
from scripts.game_logic.wave_system import WaveSystem
from scripts.game_logic.money import Money
from scripts.menus.main_menu import MainMenu

class Game:

    # Farbe vom Hintergrund (dunkelgrau)
    COLOR_BACKGROUND: tuple = (85, 85, 85)
    # blockiert rendern von schwarzer Farbe
    COLORKEY: tuple = (0, 0, 0)

    # Konstanten fuer den Spielzustand
    MAIN_MENU: str = "main menu"
    PLAYING: str = "playing"

    def __init__(self) -> None:
        """
        Beinhaltet grundlegend das Fenster und kuemmert sich um die Funktionen der anderen Klassen, fungiert als Main Datei
        """
        # initialisiert pygame und alle darin enthaltenen Module
        pygame.init()
        # setzt den Titel vom Fenster
        pygame.display.set_caption("Meteor Shooter of Absolute Doom")

        # screen initialisieren und groesse setzen
        self.screen_size: tuple = (1000, 850)
        self.screen_middle: tuple = (self.screen_size[0] / 2, self.screen_size[1] / 2)
        self.screen: pygame.Surface = pygame.display.set_mode(self.screen_size)

        # gameclock fuer fps und delta time
        self.clock: pygame.time.Clock = pygame.time.Clock()
        self.dt: float = 0

        # Tank initialisieren
        self.tank: Tank = Tank(self.screen_middle[0] - 45, self.screen_size[1] - 110)

        # Ammo initialisieren
        self.ammo: Ammo = Ammo(self.tank.pos[0], self.tank.pos[1], self)

        # Meteor initialisieren
        self.meteor: Meteor = Meteor(0, 0, self)

        # EventHandler initialisieren
        self.event_handler: EventHandler = EventHandler(self)

        # WaveSystem initialisieren
        self.wave_system: WaveSystem = WaveSystem(self)

        # Geld initialisieren
        self.money: Money = Money()

        # Menu initialisieren
        self.menu: MainMenu = MainMenu(self)

        # derzeitiger Spielzustand, startet im Hautptmenue
        self.game_state: str = self.MAIN_MENU

    
    def handle_events(self) -> None:
        """ Handhabung von Events """
        self.event_handler.key_events()

        if self.event_handler.collisions():
            # Geld hoch
            self.money.add_money(100)

    
    def run(self) -> None:
        """ der Startknopf fuer das Spiel """
        while True:
            # delta time des vergangenen Frames in Sekunden ausrechnen
            self.dt = self.clock.tick(60) / 1000.0

            keys = pygame.key.get_pressed()
            
            if self.game_state == self.MAIN_MENU:
                self.event_handler.key_events()
                # Hauptmenue laden
                self.menu.load_main_menu(self.screen)

            if self.game_state == self.PLAYING:
                self.handle_events()

                # vorheriges Frame loeschen
                self.screen.fill(self.COLOR_BACKGROUND)

                # Geld und Wellenzaehler anzeigen
                self.money.show_money(self.screen, self.screen_middle[0], self.screen_middle[1])
                self.wave_system.draw(self.screen, self.screen_middle[0], self.screen_middle[1])

                # Wellenlogik
                self.wave_system.update(self.dt)
                if self.wave_system.can_spawn(self.dt):
                    self.meteor.add()

                # Spielentities laden und updaten
                self.meteor.draw_meteor(self.screen)
                self.tank.draw_tank(self.screen)
                self.tank.update(keys, self.screen_size[0], self.dt)
                self.ammo.draw_ammo(self.screen)

                # Bild rendern
                pygame.display.update()

Game().run()