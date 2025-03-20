import pygame
import random

class MoveTexto:
    def __init__(self, texto, fonte, tamanho, cor, x, y, screen_width, screen_height):
        self.texto = texto
        self.fonte = pygame.font.Font(fonte, tamanho)
        self.cor = cor
        self.x = x
        self.y = y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.surface = self.fonte.render(self.texto, True, self.cor)
        self.rect = self.surface.get_rect(topleft=(self.x, self.y))

        # Velocidade inicial
        self.speed_x = self._non_zero()
        self.speed_y = self._non_zero()

    def _non_zero(self):
        """Gera um valor aleatório diferente de zero para a velocidade."""
        return random.choice([-2, -1, 1, 2])

    def _change_color(self):
        """Altera a cor ao bater nas bordas."""
        self.cor = (
            random.randint(10, 255),
            random.randint(10, 255),
            random.randint(10, 255),
        )
        self.surface = self.fonte.render(self.texto, True, self.cor)

    def quicar_nas_bordas(self):
        """Atualiza a posição e faz o texto quicar nas bordas."""
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect.topleft = (self.x, self.y)

        if self.x <= 0 or self.x + self.surface.get_width() >= self.screen_width:
            self.speed_x *= -1
            self._change_color()

        if self.y <= 0 or self.y + self.surface.get_height() >= self.screen_height:
            self.speed_y *= -1
            self._change_color()

    def draw(self, screen):
        """Desenha o texto na tela."""
        screen.blit(self.surface, self.rect)

    def update(self):
        """Método genérico para atualizar o texto (pode ser sobrescrito)."""
        self.quicar_nas_bordas()
