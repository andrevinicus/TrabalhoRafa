from src.MoveTexto import MoveTexto

class DVDHorizontal(MoveTexto):
    """
    Classe que representa um texto que se move apenas na horizontal,
    quicando nas laterais da tela.
    """
    
    def __init__(self, text: str, font_size: int, color: tuple, screen_width: int, screen_height: int):
        """
        Inicializa o objeto com movimento apenas horizontal.
        
        :param text: Texto a ser exibido.
        :param font_size: Tamanho da fonte do texto.
        :param color: Cor do texto em formato RGB.
        :param screen_width: Largura da tela.
        :param screen_height: Altura da tela.
        """
        super().__init__(text, None, font_size, color, screen_width // 2, screen_height // 2)
        self.speed_x = self._non_zero()
        self.speed_y = 0
    
    def update(self):
        """
        Atualiza a posição do texto, garantindo que ele se mova apenas
        na horizontal e quique nas laterais.
        """
        self.x += self.speed_x
        self.rect.x = self.x

        if self.rect.left <= 0 or self.rect.right >= self.screen_width:
            self.speed_x *= -1
            self._change_color()
