from src.MoveTexto import MoveTexto

class DVD(MoveTexto):
    def __init__(self, text, font_size, color, screen_width, screen_height):
        super().__init__(text, None, font_size, color, screen_width // 2, screen_height // 2, screen_width, screen_height)

    def update(self):
        """Apenas chama o update da superclasse."""
        super().update()
