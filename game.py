import pygame

from scripts.entities.tank import Tank
from scripts.entities.ammo import Ammo
from scripts.entities.meteor import Meteor
from scripts.event_handler import EventHandler
from scripts.timer import Timer
from scripts.money import Money
from scripts.menus.main_menu import MainMenu

class Game:

    # Farbe vom Hintergrund (dunkelgrau)
    COLOR_BACKGROUND: tuple = (85, 85, 85)
    # fungiert als Blocken vom rendern von schwarzer Farbe, damit Hintergrund in den Sprites durchsichtig erscheint
    COLORKEY: tuple = (0, 0, 0)

    # Konstanten für den Spielzustand
    MAIN_MENU: str = "main menu"
    PLAYING: str = "playing"

    def __init__(self) -> None:
        """
        Beinhaltet grundlegend das Fenster und kümmert sich um die Funktionen der anderen Klassen, fungiert als Main Datei
        """
        # initialisiert pygame und alle darin enthaltenen Module
        pygame.init()
        # setzt den Titel vom Fenster
        pygame.display.set_caption("Meteor Shooter of Absolute Doom")

        # screen initialisieren und größe setzen
        self.screen_size: tuple = (1000, 850)
        self.screen_middle: tuple = (self.screen_size[0] / 2, self.screen_size[1] / 2)
        self.screen: pygame.Surface = pygame.display.set_mode(self.screen_size)

        # gameclock fuer fps
        self.clock: pygame.time.Clock = pygame.time.Clock()

        # Tank initialisieren
        self.tank: Tank = Tank(self.screen_middle[0] - 45, self.screen_size[1] - 100)

        # Ammo initialisieren
        self.ammo: Ammo = Ammo(self.tank.pos[0], self.tank.pos[1], self)

        # Meteor initialisieren
        self.meteor: Meteor = Meteor(0, 0, self)

        # EventHandler initialisieren
        self.event_handler: EventHandler = EventHandler(self)

        # timerManager initialisieren
        self.timer: Timer = Timer()

        # Geld initialisieren
        self.money: Money = Money()

        # Menu initialisieren
        self.menu: MainMenu = MainMenu(self)

        # derzeitiger Spielzustand, startet im Hautptmenü
        self.game_state: str = self.MAIN_MENU

    
    def handle_events(self) -> None:
        """ Handhabung von Events """
        self.event_handler.key_events()

        # score inkrementieren, wenn collision auftritt zwischen meteor und ammo
        if self.event_handler.ammo_collisions():
            # Geld hoch
            self.money.add_money(100)

    
    def run(self) -> None:
        """ der Startknopf für das Spiel """
        while True:
            keys = pygame.key.get_pressed()
            if self.game_state == self.MAIN_MENU:
                self.event_handler.key_events()
                self.menu.load_main_menu(self.screen)
                self.clock.tick(60)

            if self.game_state == self.PLAYING:
                #keys = pygame.key.get_pressed()
                self.handle_events()
                self.screen.fill(self.COLOR_BACKGROUND) # loescht das vorherige Frame, damit neu gerendert werden kann
                self.money.show_money(self.screen, self.screen_middle[0], self.screen_middle[1])
                now = pygame.time.get_ticks()
                if self.timer.can_spawn(now):
                    self.meteor.add()
                self.meteor.draw_meteor(self.screen)
                self.tank.draw_tank(self.screen)
                self.tank.update(keys, self.screen_size[0])
                self.ammo.draw_ammo(self.screen)
                pygame.display.update()
                self.clock.tick(60) # fungiert als dynaischer sleep, damit die Schleife nur 60 mal pro sek. aufgerufen wird

Game().run()