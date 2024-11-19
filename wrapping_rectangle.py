import sys
import pygame

# Wrapped immer am jeweiligen Ende vom Spieler und baut ihn auf der anderen Seite direkt ganz auf
class WrappingRectangle1:

    COLOR_RECT = (0, 0, 200)
    COLOR_BACKGROUND = (255, 255, 255)
    COLOR_AMMO = (255, 0, 0)
    #moving = False
    ammo_shot = False

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Moving Rectangle")
        self.screen_size = (1280, 720)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.clock = pygame.time.Clock()
        self.rect_pos = [(self.screen_size[0] / 2) - 50, (self.screen_size[1] - 50) - 25]
        self.rect_dimensions = [100, 50]
        # ammo hat hierdurch beim schießen permanent die Koordinaten vom Panzer, wenn er sich bewegt
        self.ammo_pos = [self.rect_pos[0] + ((self.rect_dimensions[0] / 2) - 50), self.rect_pos[1] + ((self.rect_dimensions[1] / 2) - 25)]


    def draw_rect(self) -> None:
        pygame.draw.rect(self.screen, self.COLOR_RECT, pygame.Rect(self.rect_pos[0], self.rect_pos[1],  self.rect_dimensions[0], self.rect_dimensions[1]))


    def move_rect(self) -> None:
        self.key_input = pygame.key.get_pressed()
        if self.key_input[pygame.K_RIGHT]:
            self.rect_pos[0] += 5
        if self.key_input[pygame.K_LEFT]:
            self.rect_pos[0] -= 5

        if self.rect_pos[0] + self.rect_dimensions[0] < 0:
            self.rect_pos[0] = self.screen_size[0] - self.rect_dimensions[0]
        elif self.rect_pos[0] > self.screen_size[0]:
            self.rect_pos[0] = 0


    def draw_ammo(self) -> None:
        pygame.draw.rect(self.screen, self.COLOR_AMMO, pygame.Rect(self.ammo_pos[0], self.ammo_pos[1], 20, 20))


    def shoot_ammo(self) -> None:
        self.ammo_pos[1] -= 13


    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # nur event gibt <Event(256-Quit {})> wieder, event.type ein int
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.ammo_shot = True
                    print(f"{self.ammo_pos[0]} + {self.ammo_pos[1]}")

        self.move_rect()


    def run(self) -> None:
        while True:
            self.handle_events()
            self.screen.fill(self.COLOR_BACKGROUND) # !!! WICHTIG DAMIT ALTEN FRAMES GELÖSCHT WERDEN !!!
            self.draw_rect()
            self.ammo_pos[0] = (self.rect_dimensions[0] / 2) + self.rect_pos[0] - 10
            if self.ammo_shot == True:
                self.draw_ammo()
                self.shoot_ammo()
            pygame.display.update()
            self.clock.tick(60)


# Wrapped immer am jeweiligen Ende des Spielers und baut sich aber am anderen Rand komplett neu auf
class WrappingRectangle2:
    COLOR_RECT = (0, 0, 200)
    COLOR_BACKGROUND = (255, 255, 255)
    COLOR_AMMO = (255, 0, 0)
    #moving = False
    ammo_shot = False

    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Moving Rectangle")
        self.screen_size = (1280, 720)
        self.screen = pygame.display.set_mode(self.screen_size)
        self.clock = pygame.time.Clock()
        self.rect_pos = [(self.screen_size[0] / 2) - 50, (self.screen_size[1] - 50) - 25]
        self.rect_dimensions = [100, 50]
        # ammo hat hierdurch beim schießen permanent die Koordinaten vom Panzer, wenn er sich bewegt
        self.ammo_pos = [self.rect_pos[0] + ((self.rect_dimensions[0] / 2) - 50), self.rect_pos[1] + ((self.rect_dimensions[1] / 2) - 25)]


    def draw_rect(self) -> None:
        pygame.draw.rect(self.screen, self.COLOR_RECT, pygame.Rect(self.rect_pos[0], self.rect_pos[1],  self.rect_dimensions[0], self.rect_dimensions[1]))


    def move_rect(self) -> None:
        self.key_input = pygame.key.get_pressed()
        if self.key_input[pygame.K_RIGHT]:
            self.rect_pos[0] += 5
        if self.key_input[pygame.K_LEFT]:
            self.rect_pos[0] -= 5

        if self.rect_pos[0] + self.rect_dimensions[0] < 0:
            self.rect_pos[0] = self.screen_size[0]
        elif self.rect_pos[0] > self.screen_size[0]:
            self.rect_pos[0] = 0 - self.rect_dimensions[0]


    def draw_ammo(self) -> None:
        pygame.draw.rect(self.screen, self.COLOR_AMMO, pygame.Rect(self.ammo_pos[0], self.ammo_pos[1], 20, 20))


    def shoot_ammo(self) -> None:
        self.ammo_pos[1] -= 13


    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # nur event gibt <Event(256-Quit {})> wieder, event.type ein int
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.ammo_shot = True
                    print(f"{self.ammo_pos[0]} + {self.ammo_pos[1]}")

        self.move_rect()


    def run(self) -> None:
        while True:
            self.handle_events()
            self.screen.fill(self.COLOR_BACKGROUND) # !!! WICHTIG DAMIT ALTEN FRAMES GELÖSCHT WERDEN !!!
            self.draw_rect()
            self.ammo_pos[0] = (self.rect_dimensions[0] / 2) + self.rect_pos[0] - 10
            if self.ammo_shot == True:
                self.draw_ammo()
                self.shoot_ammo()
            pygame.display.update()
            self.clock.tick(60)


WrappingRectangle2().run()