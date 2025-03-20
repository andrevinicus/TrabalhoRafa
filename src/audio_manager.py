import pygame

class AudioManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {
            "bounce": pygame.mixer.Sound("assets/bounce.wav")  # Som ao bater na borda
        }
        self.music_files = [
            "assets/music1.mp3",
            "assets/music2.mp3"
        ]
        self.current_music_index = 0
        self.music_playing = False
        
        # Carregar e iniciar a primeira música
        pygame.mixer.music.load(self.music_files[self.current_music_index])
        pygame.mixer.music.set_volume(2)  # Define volume da música

    def play_sound(self, sound_name):
        if sound_name in self.sounds:
            self.sounds[sound_name].play()

    def play_music(self):
        if not self.music_playing:
            pygame.mixer.music.play(-1)  # Loop infinito
            self.music_playing = True

    def stop_music(self):
        pygame.mixer.music.stop()
        self.music_playing = False

    def toggle_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            self.music_playing = False
        else:
            pygame.mixer.music.unpause()
            self.music_playing = True

    def next_music(self):
        self.current_music_index = (self.current_music_index + 1) % len(self.music_files)
        pygame.mixer.music.load(self.music_files[self.current_music_index])
        pygame.mixer.music.play(-1)  # Loop infinito
        self.music_playing = True
