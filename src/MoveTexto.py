import pygame

class MoveTexto:
    def __init__(self, texto, fonte, tamanho, cor, x, y):
        self.texto = texto
        self.fonte = pygame.font.Font(fonte, tamanho)
        self.cor = cor
        self.x = x
        self.y = y
        self.surface = self.fonte.render(self.texto, True, self.cor)
        self.rect = self.surface.get_rect(topleft=(self.x, self.y))

    def draw(self, screen):
        """ Desenha o texto na tela """
        screen.blit(self.surface, self.rect)

    def update(self):
        """ Método genérico para atualizar a posição ou estado do texto (deve ser sobrescrito pelas subclasses) """
        pass
