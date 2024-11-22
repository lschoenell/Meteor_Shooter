import pygame

class SpriteManager:

    def __init__(self) -> None:
        """
        initialisiert den Sprite Manager mit einem leeren cache, damit bei mehrfachen aufrufen der pygame.image.load() Funktion nur einmal das Bild geladen werden muss und sonst aus dem cache genommen wird
        """
        self.sprites = {}

    def load_sprite(self, path: str, dimensions: tuple) -> pygame.Surface:
        """
        läd und skaliert einen Sprite vom gegebenen Pfad falls noch nicht vorhanden, ansonsten wird der gesuchte Sprite aus dem cache returned

        Arguments:
            path (str): der Pfad zum Bild
            dimensions (tuple): die Dimensionen (Breite, Höhe) für die Skalierung

        Returns:
            pygame.Surface: den Sprite
        """
        if path not in self.sprites:
            sprite = pygame.image.load(path).convert()  # Optimize for display
            sprite = pygame.transform.scale(sprite, dimensions)
            self.sprites[path] = sprite
        return self.sprites[path]