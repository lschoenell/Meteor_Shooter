import sys
import pygame

class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Ninja Game")
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()

    # run wichtig mit endlosloop weil sonst programm terminiert und das Fenster nur kurz angezeigt wird, bis es wieder geschlossen wird
    def run(self) -> None:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # nur event gibt <Event(256-Quit {})> wieder, event.type ein int
                    pygame.quit()
                    sys.exit()
                
            self.screen.fill((0, 0, 0))
            pygame.display.update()
            self.clock.tick(60) # im Prinzip ein sleeptimer damit das nur 60 mal pro Sekunde aufgerufen wird
                

Game().run()