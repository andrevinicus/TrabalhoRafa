from src.MoveTexto import MoveTexto

class DVDVertical(MoveTexto):
    def __init__(self, text, font_size, color, screen_width, screen_height):
        super().__init__(text, None, font_size, color, screen_width // 2, screen_height // 2)
        self.speed_x = 0  # Mantém o movimento horizontal zerado
        self.speed_y = self._non_zero()  # Apenas movimento vertical

    def update(self):
        """Move apenas na vertical e quica no topo e base da tela"""
        self.y += self.speed_y
        self.rect.y = self.y  # Atualiza a posição do retângulo

        if self.rect.top <= 0 or self.rect.bottom >= self.screen_height:
            self.speed_y *= -1
            self._change_color()
