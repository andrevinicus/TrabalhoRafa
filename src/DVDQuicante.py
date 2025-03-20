from src.MoveTexto import MoveTexto

class TextoQuicante(MoveTexto):
    def __init__(self, text, font_size, color, screen_width, screen_height):
        super().__init__(text, None, font_size, color, screen_width // 2, screen_height // 2, screen_width, screen_height)

    def update(self):
        """Atualiza a posição e faz o texto quicar nas bordas"""
        super().update()  # Usa a lógica da superclasse
