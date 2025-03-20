from src.MoveTexto import MoveTexto

class DVD(MoveTexto):
    """
    Representa um objeto de texto que se move na tela, 
    herdando o comportamento de MoveTexto.
    """
    def __init__(self, text, font_size, color, screen_width, screen_height):
        """
        Inicializa o objeto DVD.

        :param text: Texto a ser exibido.
        :param font_size: Tamanho da fonte do texto.
        :param color: Cor do texto.
        :param screen_width: Largura da tela.
        :param screen_height: Altura da tela.
        """
        super().__init__(text, None, font_size, color, screen_width // 2, screen_height // 2, screen_width, screen_height)

    def update(self):
        """
        Atualiza a posição do objeto chamando o método da superclasse.
        """
        super().update()
