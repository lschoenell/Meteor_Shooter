import pygame

class Timer:

    def __init__(self) -> None:
        """ Initialisiert den Timer, setzt den timer auf 0 und setzt die Schwierigkeit """
        self.last_spawn_time: int = 0
        # respawn timer, 1000 Millisekunden sind 1 Sekunde
        self.difficulty : int = 1000

    
    def can_spawn(self, current_time: int) -> bool:
        """
        checkt, ob genug Zeit im gameloop vergangen ist, dass der respawn timer überschritten wird
        Arguments:
            current_time (int): die jetzige Zeit im gameloop, kann geholt werden durch pygame.timer.get_ticks()
        Returns:
            bool: ob neu gespawnt werden kann oder nicht
        """
        if current_time - self.last_spawn_time > self.difficulty:
            self.last_spawn_time = current_time
            return True
        else:
            return False