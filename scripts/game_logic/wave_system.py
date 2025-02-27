import pygame

class WaveSystem:

    def __init__(self) -> None:
        """initialisiert die fuer die Wellen wichtigen Werte"""
        # alles in Sekunden
        self.wave_duration: float = 10.0
        self.wave_cooldown: float = 5.0
        self.wave_timer: float = 0.0
        self.wave_active: bool = True
        self.current_wave: int = 0
        self.spawn_rate: float = 1.0
        self.spawn_timer: float = 0.0


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
        else:
            self.wave_timer += dt
            if self.wave_timer >= self.wave_cooldown:
                self.wave_active = True
                self.wave_timer = 0
                self.current_wave += 1
                self.spawn_rate = max(0.2, 1.0 - (self.current_wave * 0.1))


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