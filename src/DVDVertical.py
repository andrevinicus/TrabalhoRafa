from src.dvd import DVD

class DVDVertical(DVD):
    def __init__(self, text, font_size, color, screen_width, screen_height):
        super().__init__(text, font_size, color, screen_width, screen_height)
        self.speed_y = self._non_zero()  # Apenas movimento vertical

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top <= 0 or self.rect.bottom >= self.screen_height:
            self.speed_y *= -1
            self._change_color()
