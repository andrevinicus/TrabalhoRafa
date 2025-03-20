# Jogo de Texto em Movimento

## Descrição
Este projeto simula um texto se movendo pela tela no estilo "DVD", quicando nas bordas e mudando de cor ao colidir. Além disso, inclui recursos de áudio, como efeitos sonoros e música de fundo, e foi estruturado seguindo os princípios de Clean Code e SOLID.

## Funcionalidades
- Texto animado que quica nas bordas.
- Movimentos específicos (horizontal, vertical e aleatório).
- Mudança de cor ao colidir.
- Reprodução de efeitos sonoros.
- Música de fundo com controles para troca e pausa.

## Estrutura do Código

### Principais Arquivos
- `game.py` - Gerencia a lógica principal do jogo.
- `MoveTexto.py` - Superclasse responsável pelo movimento do texto.
- `DVDQuicante.py` - Texto que quica e muda de cor.
- `DVDHorizontal.py` - Texto que se move apenas na horizontal.
- `DVDVertical.py` - Texto que se move apenas na vertical.
- `dvd.py` - Classe base que apenas chama a atualização do movimento.
- `audio_manager.py` - Gerencia os sons e a música do jogo.
- `config.py` - Configurações globais do jogo.

## Diagrama UML
O projeto conta com um diagrama UML que representa a estrutura das classes, evidenciando a relação de herança entre `MoveTexto` e suas subclasses (`DVDQuicante`, `DVDHorizontal`, `DVDVertical`).

## Princípios Aplicados
- **Clean Code**: Código modular, bem organizado e com nomes descritivos.
- **SOLID**: Uso da herança para reuso de código e separação de responsabilidades.

## Como Executar
1. Certifique-se de ter o Python e a biblioteca `pygame` instalados:
   ```sh
   pip install pygame
   ```
2. Execute o jogo com:
   ```sh
   python game.py
   ```

## Controles
- `S` - Troca a música.
- `SPACE` - Pausa ou retoma a música.
- `Fechar a janela` - Encerra o jogo.