import sys
import pygame

class OneTimeButtonPress:

    moving = False

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

                if event.type == pygame.KEYDOWN:
                    print("Eine Taste wurde gedrückt")
                    self.moving = True
                    print(self.moving)

                if event.type == pygame.KEYUP:
                    print("Eine Taste wurde losgelassen")
                    self.moving = False
                    print(self.moving)
                
            pygame.display.update()
            self.clock.tick(60) # im Prinzip ein sleeptimer damit das nur 60 mal pro Sekunde aufgerufen wird
                

class ContinuousButtonPress:

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
                
            key = pygame.key.get_pressed()
            if key[pygame.K_LEFT]:
                print("Links gedrückt")

            if key[pygame.K_RIGHT]:
                print("Rechts gedrückt")

            pygame.display.update()
            self.clock.tick(60) # im Prinzip ein sleeptimer damit das nur 60 mal pro Sekunde aufgerufen wird
                

class ShootingRect:

    rect_position = [1280 / 2, 700]
    rect_shot = False

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Ninja Game")
        self.screen = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()


    def draw_rect(self) -> None:
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.rect_position[0], self.rect_position[1], 50, 50))

    def shoot_rect(self) -> None:
        self.rect_position[1] -= 5

    # run wichtig mit endlosloop weil sonst programm terminiert und das Fenster nur kurz angezeigt wird, bis es wieder geschlossen wird
    def run(self) -> None:
        while True:
            self.screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # nur event gibt <Event(256-Quit {})> wieder, event.type ein int
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.rect_shot = True

            if self.rect_shot == True:
                self.draw_rect()
                self.shoot_rect()            
            
            pygame.display.update()
            self.clock.tick(60) # im Prinzip ein sleeptimer damit das nur 60 mal pro Sekunde aufgerufen wird
          
# Was noch fehlt: Implementation von Grenzen, damit Rechteck nicht unendlich weiter fliegt
# Implementation von mehreren Rechtecken die gleichzeitig fliegen können


ShootingRect().run()