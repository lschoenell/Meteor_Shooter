import pygame

class WaveSystem:

    COLOR_WAVE_TEXT: tuple = (125, 125, 120)

    def __init__(self) -> None:
        """initialisiert die fuer die Wellen wichtigen Werte"""
        # alles in Sekunden
        self.wave_duration: float = 10.0
        self.wave_timer: float = 0.0
        self.wave_active: bool = True
        self.current_wave: int = 1
        self.spawn_rate: float = 1.0
        self.spawn_timer: float = 0.0

        # Text fuer Wellenzaehler
        self.font: pygame.font.Font = pygame.font.Font(None, 50)
        self.wave_text: pygame.Surface = None
        self.update_wave_text()


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


    def show_wave_counter(self, screen: pygame.Surface, x: int, y:int) -> None:
        screen.blit(self.wave_text, (x - (self.wave_text.get_width() / 2), y - (self.wave_text.get_height() / 2 ) + 115))