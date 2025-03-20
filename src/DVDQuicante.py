import random
import time
from src.MoveTexto import MoveTexto

class TextoQuicante(MoveTexto):
    """
    Representa um texto que se move pela tela e quica nas bordas, alterando aleatoriamente sua direção a cada intervalo de tempo.
    
    Attributes:
        last_direction_change (float): Momento da última mudança de direção.
    """
    
    def __init__(self, text, font_size, color, screen_width, screen_height, audio_manager):
        """
        Inicializa o texto quicante.

        Args:
            text (str): Texto exibido.
            font_size (int): Tamanho da fonte.
            color (tuple): Cor do texto em RGB.
            screen_width (int): Largura da tela.
            screen_height (int): Altura da tela.
            audio_manager (AudioManager): Gerenciador de áudio para reprodução de sons.
        """
        super().__init__(text, None, font_size, color, screen_width // 2, screen_height // 2, screen_width, screen_height, audio_manager)
        self.last_direction_change = time.time()

    def _change_direction(self):
        """
        Altera a direção do movimento aleatoriamente.
        """
        self.speed_x = random.choice([-abs(self.speed_x), abs(self.speed_x)])
        self.speed_y = random.choice([-abs(self.speed_y), abs(self.speed_y)])

    def update(self):
        """
        Atualiza a posição do texto e faz com que ele quique nas bordas.
        """
        super().update()

        if time.time() - self.last_direction_change >= 3:
            self._change_direction()
            self.last_direction_change = time.time()