from src.MoveTexto import MoveTexto

class DVDHorizontal(MoveTexto):
    def __init__(self, text, font_size, color, screen_width, screen_height):
        super().__init__(text, None, font_size, color, screen_width // 2, screen_height // 2)
        self.speed_x = self._non_zero()  # Apenas movimento horizontal
        self.speed_y = 0  # Mantém o movimento vertical zerado

    def update(self):
        """Move apenas na horizontal e quica nas laterais"""
        self.x += self.speed_x
        self.rect.x = self.x  # Atualiza a posição do retângulo

        if self.rect.left <= 0 or self.rect.right >= self.screen_width:
            self.speed_x *= -1
            self._change_color()
