import random
import time
from src.MoveTexto import MoveTexto

class TextoQuicante(MoveTexto):
    def __init__(self, text, font_size, color, screen_width, screen_height):
        super().__init__(text, None, font_size, color, screen_width // 2, screen_height // 2, screen_width, screen_height)
        self.last_direction_change = time.time()  # Guarda o tempo da última mudança de direção

    def _change_direction(self):
        """Muda a direção do movimento aleatoriamente."""
        self.speed_x = random.choice([-abs(self.speed_x), abs(self.speed_x)])  # Mantém módulo, mas troca sinal
        self.speed_y = random.choice([-abs(self.speed_y), abs(self.speed_y)])

    def update(self):
        """Atualiza a posição e faz o texto quicar nas bordas"""
        super().update()  # Usa a lógica da superclasse

        # Muda a direção a cada 10 segundos
        if time.time() - self.last_direction_change >= 3:
            self._change_direction()
            self.last_direction_change = time.time()
