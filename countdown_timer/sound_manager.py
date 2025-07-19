import pygame
import os

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.sounds = {
            "default": os.path.join("assets", "default_sound.mp3"),
        }
        self.current_sound = self.sounds["default"]

    def load_default_sounds(self):
        ringtone_dir = os.path.expanduser("~/Music/CustomRingtones/")
        if not os.path.exists(ringtone_dir):
            os.makedirs(ringtone_dir)
        for file_name in os.listdir(ringtone_dir):
            if file_name.endswith((".mp3", ".wav")):
                self.add_custom_sound(os.path.join(ringtone_dir, file_name))

    def add_custom_sound(self, sound_path):
        if os.path.exists(sound_path):
            sound_name = os.path.basename(sound_path)
            self.sounds[sound_name] = sound_path
        else:
            raise ValueError("文件不存在")

    def play_sound_loop(self):
        pygame.mixer.music.load(self.current_sound)
        pygame.mixer.music.play(loops=-1)

    def stop_sound(self):
        pygame.mixer.music.stop()

    def set_sound(self, sound_path):
        if os.path.exists(sound_path):
            self.current_sound = sound_path
        else:
            raise ValueError("铃声文件不存在")
