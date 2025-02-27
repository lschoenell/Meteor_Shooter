import pygame

class WaveSystem:

    def __init__(self) -> None:
        """initialisiert die fuer die Wellen wichtigen Werte"""
        # alles in Sekunden
        self.wave_duration = 10.0
        self.wave_cooldown = 5.0
        self.wave_timer = 0.0
        self.wave_active = False
        self.current_wave = 0
        self.spawn_rate = 1.0
        self.spawn_timer = 0

    def update(self, dt: float) -> None:

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

        if not self.wave_active:
            return False

        self.spawn_timer += dt
        if self.spawn_timer >= self.spawn_rate:
            self.spawn_timer = 0
            return True
        return False