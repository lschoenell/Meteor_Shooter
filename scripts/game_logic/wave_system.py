import pygame
from scripts.power_ups import Power_Ups
from scripts.sprite_manager import SpriteManager

class WaveSystem:

    COLOR_WAVE_TEXT: tuple = (125, 125, 120)
    POWERUP_TEXT: str = "Buy phase!"
    POWERUP_TEXT_COLOR: tuple = (200, 200, 200)

    def __init__(self, game: object) -> None:
        """initialisiert die fuer die Wellen wichtigen Werte"""
        self.game: object = game
        self.powerups: Power_Ups = Power_Ups(self.game)
        self.sprite_manager: SpriteManager = SpriteManager()

        # alles in Sekunden
        self.wave_duration: float = 10.0
        self.wave_timer: float = 0.0
        self.wave_active: bool = True
        self.current_wave: int = 1
        self.spawn_rate: float = 1.0
        self.spawn_timer: float = 0.0
        self.in_powerup_selection: bool = False

        # Text fuer Wellenzaehler und Power-Up Auswahlphase
        self.font: pygame.font.Font = pygame.font.Font(None, 50)
        self.wave_text: pygame.Surface = None
        self.powerup_phase_text: pygame.Surface = self.font.render(self.POWERUP_TEXT, True, self.POWERUP_TEXT_COLOR)
        self.update_wave_text()

        # Button um zu naechsten Wave zu kommen
        self.next_button: pygame.Surface = self.sprite_manager.load_sprite("assets/ui/Next_Button.png", (160, 80))
        self.next_button_pos: tuple = (self.game.screen_size[0] - (100 + self.next_button.get_width()), self.game.screen_size[1] - 200)
        self.next_button_rect: pygame.Rect = self.next_button.get_rect()
        self.next_button_rect.topleft = self.next_button_pos
        self.next_button_hover: pygame.Surface = self.sprite_manager.load_sprite("assets/ui/Next_Button_Hover.png", (160, 80))


    def update_wave_text(self) -> None:
        """updated den Text der Wellennummer basierend auf der derzeitigen Nummer der Welle und setzt die Alpha auf 125"""
        self.wave_text = self.font.render(f"Wave: {self.current_wave}", True, self.COLOR_WAVE_TEXT).convert_alpha()
        self.wave_text.set_alpha(125)


    def update(self, dt: float) -> None:
        """
        updated die Zeiten die Zeiten der Welle und wechselt zwischen Pause und Welle basierend auf der vergangenen Zeit

        Arguments:
        ---------
            dt (float): delta time in Sekunden
        """
        if self.wave_active:
            self.wave_timer += dt
            if self.wave_timer >= self.wave_duration:
                self.wave_active = False
                self.wave_timer = 0
                self.spawn_rate = max(0.2, 1.0 - (self.current_wave * 0.17))
                self.current_wave += 1
                self.in_powerup_selection = True
                self.update_wave_text()


    def can_spawn(self, dt: float) -> bool:
        """
        checkt, ob genug Zeit vergangen ist, um einen neuen Meteoriten zu spawnen
        
        Arguments:
        ---------
            dt (float): delta time in Sekunden
        """
        if not self.wave_active:
            return False

        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_rate:
            self.spawn_timer = 0
            return True
        return False


    def draw(self, screen: pygame.Surface, x: int, y:int) -> None:
        
        if self.wave_active == True:
            screen.blit(self.wave_text, (x - (self.wave_text.get_width() / 2), y - (self.wave_text.get_height() / 2 ) + 115))

        if self.in_powerup_selection == True:
            screen.blit(self.powerup_phase_text, (x - (self.powerup_phase_text.get_width() / 2), y - (self.powerup_phase_text.get_height() / 2 ) + 130))
            self.powerups.draw(screen)
            if self.next_button_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(self.next_button_hover, self.next_button_pos)
            else:
                screen.blit(self.next_button, self.next_button_pos)