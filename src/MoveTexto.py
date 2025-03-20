import pygame
import random
import time

class MoveTexto:
    """
    Classe responsável por mover um texto na tela, fazendo-o quicar nas bordas e mudar de cor ao colidir.
    """
    def __init__(self, texto, fonte, tamanho, cor, x, y, screen_width, screen_height, audio_manager):
        """
        Inicializa um objeto MoveTexto.

        Parâmetros:
        - texto (str): O texto a ser exibido.
        - fonte (str ou None): Caminho para a fonte ou None para a fonte padrão.
        - tamanho (int): Tamanho da fonte.
        - cor (tuple): Cor do texto em formato RGB.
        - x (int): Posição inicial no eixo X.
        - y (int): Posição inicial no eixo Y.
        - screen_width (int): Largura da tela.
        - screen_height (int): Altura da tela.
        - audio_manager (AudioManager): Objeto responsável pelo gerenciamento de áudio.
        """
        self.texto = texto
        self.fonte = pygame.font.Font(fonte, tamanho)
        self.cor = cor
        self.x = x
        self.y = y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.surface = self.fonte.render(self.texto, True, self.cor)
        self.rect = self.surface.get_rect(topleft=(self.x, self.y))

       
        self.speed_x = self._non_zero()
        self.speed_y = self._non_zero()

       
        self.audio_manager = audio_manager

    def _non_zero(self):
        """
        Gera um valor aleatório diferente de zero para a velocidade.

        Retorno:
        - (int): Um valor aleatório entre -2 e 2, excluindo o zero.
        """
        return random.choice([-2, -1, 1, 2])

    def _change_color(self):
        """
        Altera a cor do texto aleatoriamente ao bater nas bordas.
        """
        self.cor = (
            random.randint(10, 255),
            random.randint(10, 255),
            random.randint(10, 255),
        )
        self.surface = self.fonte.render(self.texto, True, self.cor)

    def quicar_nas_bordas(self):
        """
        Atualiza a posição do texto e verifica colisões com as bordas da tela.
        Ao bater, muda de direção, altera a cor e toca um som.
        """
        self.x += self.speed_x
        self.y += self.speed_y
        self.rect.topleft = (self.x, self.y)

        if self.x <= 0 or self.x + self.surface.get_width() >= self.screen_width:
            self.speed_x *= -1
            self._change_color()
            self.audio_manager.play_sound("bounce")  

        if self.y <= 0 or self.y + self.surface.get_height() >= self.screen_height:
            self.speed_y *= -1
            self._change_color()
            self.audio_manager.play_sound("bounce")  

    def draw(self, screen):
        """
        Desenha o texto na tela.

        Parâmetros:
        - screen (pygame.Surface): Superfície onde o texto será desenhado.
        """
        screen.blit(self.surface, self.rect)

    def update(self):
        """
        Atualiza a posição do texto e verifica colisões.
        """
        self.quicar_nas_bordas()
