import random
from src.dvd import DVD

class TextoQuicante(DVD):
    def __init__(self, text, font_size, color, screen_width, screen_height):
        super().__init__(text, font_size, color, screen_width, screen_height)

    def update(self):
        """Atualiza a posição e faz o texto quicar nas bordas"""
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect.topleft = (self.x, self.y)  # Atualiza a posição do rect

        if self.x <= 0 or self.x + self.surface.get_width() >= self.screen_width:
            self.speed_x *= -1
            self._change_color()

        if self.y <= 0 or self.y + self.surface.get_height() >= self.screen_height:
            self.speed_y *= -1
            self._change_color()
