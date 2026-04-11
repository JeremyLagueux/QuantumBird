import pygame
from pygame import Surface


class ParallaxLayer:
    def __init__(
        self, image_path: str, speed: float, screen_width: int, screen_height: int
    ):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (screen_width, screen_height))
        self.speed = speed
        self.x1 = 0
        self.x2 = screen_width
        self.width = screen_width

    def update(self, dt: float) -> None:
        dx = self.speed * dt
        self.x1 -= dx
        self.x2 -= dx

        if self.x1 <= -self.width:
            self.x1 = self.x2 + self.width
        if self.x2 <= -self.width:
            self.x2 = self.x1 + self.width

    def draw(self, screen: Surface) -> None:
        screen.blit(self.image, (int(self.x1), 0))
        screen.blit(self.image, (int(self.x2), 0))
