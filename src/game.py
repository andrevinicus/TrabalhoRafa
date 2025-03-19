import pygame
from src.DVDQuicante import TextoQuicante
from src.config import SCREEN_HEIGHT, SCREEN_WIDTH, FPS, PRETO

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("DVD")
        self.clock = pygame.time.Clock()
        self.running = True

        # Escolha um único movimento
        self.text = TextoQuicante("DVD", 50, (255, 255, 255), SCREEN_WIDTH, SCREEN_HEIGHT)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.text.update()

    def draw(self):
        self.screen.fill(PRETO)
        self.text.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()
