from src.dvd import DVD

class DVDHorizontal(DVD):
    def __init__(self, text, font_size, color, screen_width, screen_height):
        super().__init__(text, font_size, color, screen_width, screen_height)
        self.speed_x = self._non_zero()  # Apenas movimento horizontal

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left <= 0 or self.rect.right >= self.screen_width:
            self.speed_x *= -1
            self._change_color()
