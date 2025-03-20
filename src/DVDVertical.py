from src.MoveTexto import MoveTexto

class DVDVertical(MoveTexto):
    """
    Classe que representa um texto em movimento vertical na tela.
    O texto quica ao atingir os limites superior e inferior da tela.
    """
    
    def __init__(self, text, font_size, color, screen_width, screen_height):
        """
        Inicializa um objeto DVDVertical.

        Args:
            text (str): Texto a ser exibido.
            font_size (int): Tamanho da fonte do texto.
            color (tuple): Cor do texto em formato RGB.
            screen_width (int): Largura da tela.
            screen_height (int): Altura da tela.
        """
        super().__init__(text, None, font_size, color, screen_width // 2, screen_height // 2)
        self.speed_x = 0  # Mantém o movimento horizontal zerado
        self.speed_y = self._non_zero()  # Apenas movimento vertical

    def update(self):
        """
        Atualiza a posição do texto, permitindo apenas movimento vertical.
        O texto quica ao atingir os limites superior e inferior da tela.
        """
        self.y += self.speed_y
        self.rect.y = self.y  # Atualiza a posição do retângulo

        if self.rect.top <= 0 or self.rect.bottom >= self.screen_height:
            self.speed_y *= -1
            self._change_color()
