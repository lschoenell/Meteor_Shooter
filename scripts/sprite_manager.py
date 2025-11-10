import pygame

class SpriteManager:

    # blockiert das rendern von schwarzer Farbe, damit Hitergrund vom Sprite transparent erscheint
    COLORKEY: tuple = (0, 0, 0)

    def __init__(self) -> None:
        """
        initialisiert den Sprite Manager mit einem leeren cache, damit bei mehrfachen aufrufen der pygame.image.load() Funktion nur einmal das Bild geladen werden muss und sonst aus dem cache genommen wird
        """
        self.sprites: dict = {}

    def load_sprite(self, path: str, dimensions: tuple) -> pygame.Surface:
        """
        laed und skaliert einen Sprite vom gegebenen Pfad falls noch nicht vorhanden, ansonsten wird der gesuchte Sprite aus dem cache geladen

        Arguments:
        ---------
            path (str): der Pfad zum Bild
            dimensions (tuple): die Dimensionen (Breite, Hoehe) fuer die Skalierung

        Returns:
        -------
            pygame.Surface: den Sprite
        """
        if path not in self.sprites:
            sprite = pygame.image.load(path).convert()
            sprite = pygame.transform.scale(sprite, dimensions)
            sprite.set_colorkey(self.COLORKEY)
            self.sprites[path] = sprite
        return self.sprites[path]