import pygame
from src.DVDQuicante import TextoQuicante
from src.config import SCREEN_HEIGHT, SCREEN_WIDTH, FPS, PRETO
from src.audio_manager import AudioManager

class Game:
    """
    Classe principal do jogo que gerencia a inicialização, eventos, atualização e renderização.
    """
    
    def __init__(self):
        """
        Inicializa o jogo, criando a tela, relógio e gerenciador de áudio.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("DVD")
        self.clock = pygame.time.Clock()
        self.running = True
        self.audio_manager = AudioManager()
        self.text = TextoQuicante("DVD", 50, (255, 255, 255), SCREEN_WIDTH, SCREEN_HEIGHT, self.audio_manager)
        self.audio_manager.play_music()

    def events(self):
        """
        Captura e processa os eventos do jogo.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    self.audio_manager.next_music()
                elif event.key == pygame.K_SPACE:
                    self.audio_manager.toggle_music()

    def update(self):
        """
        Atualiza os elementos do jogo.
        """
        self.text.update()

    def draw(self):
        """
        Renderiza os elementos gráficos na tela.
        """
        self.screen.fill(PRETO)
        self.text.draw(self.screen)
        pygame.display.flip()

    def run(self):
        """
        Loop principal do jogo.
        """
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()