import random
from src.MoveTexto import MoveTexto

class DVD(MoveTexto):
    def __init__(self, text, font_size, color, screen_width, screen_height):
        super().__init__(text, None, font_size, color, screen_width // 2, screen_height // 2)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.speed_x = self._non_zero()
        self.speed_y = self._non_zero()

    def _non_zero(self):
        """Gera um valor aleatório diferente de zero para a velocidade."""
        return random.choice([-2, -1, 1, 2])

    def _change_color(self):
        """Altera a cor ao bater nas bordas."""
        self.color = (
            random.randint(10, 255),
            random.randint(10, 255),
            random.randint(10, 255),
        )
        self.surface = self.fonte.render(self.texto, True, self.color)

    def update(self):
        """A subclasse precisa sobrescrever esse método."""
        pass
