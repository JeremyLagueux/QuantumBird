from pygame import Rect, Surface, mouse, font
from typing import Callable

class Button:
    def __init__(self, rect: Rect, text: str, fun: Callable, font: font.Font | None, color: str) -> None:
        self.rect = rect
        self.text = text
        self.fun = fun
        self.color = color
        self.button_surface = Surface((rect.width, rect.height))
        if font != None:
            self.surface = font.render(text, True, (20, 20, 20))

    def process(self, screen: Surface) -> None:
        self._draw()
        if self.rect.collidepoint(mouse.get_pos()):
            if mouse.get_pressed()[0]:
                self.fun()
    
        screen.blit(self.button_surface, self.rect)

    def _draw(self) -> None:
        self.button_surface.fill(self.color)
