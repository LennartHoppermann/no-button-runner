"""
Musik-Abspieler Modul
"""

import pygame
from pathlib import Path
import os


class MusicPlayer:
    """Einfacher Musik-Player für Hintergrund-Musik"""
    
    _initialized = False
    _current_track = None
    _is_muted = False
    _volume_before_mute = 0.3
    
    @staticmethod
    def initialize():
        """Initialisiere Pygame Mixer"""
        if not MusicPlayer._initialized:
            try:
                pygame.mixer.init()
                MusicPlayer._initialized = True
                print("✓ Audio-System initialisiert")
            except Exception as e:
                print(f"Fehler beim Init Audio: {e}")
    
    @staticmethod
    def mute():
        """Stille Musik"""
        if not MusicPlayer._initialized:
            MusicPlayer.initialize()
        try:
            MusicPlayer._is_muted = True
            pygame.mixer.music.set_volume(0)
            print("🔇 Musik stummgeschaltet")
        except Exception as e:
            print(f"Fehler beim Stummschalten: {e}")
    
    @staticmethod
    def unmute():
        """Stille wieder an"""
        if not MusicPlayer._initialized:
            MusicPlayer.initialize()
        try:
            MusicPlayer._is_muted = False
            pygame.mixer.music.set_volume(MusicPlayer._volume_before_mute)
            print("🔊 Musik aktiviert")
        except Exception as e:
            print(f"Fehler beim Aktivieren: {e}")
    
    @staticmethod
    def toggle_mute():
        """Toggle Stummschaltung"""
        if MusicPlayer._is_muted:
            MusicPlayer.unmute()
        else:
            try:
                MusicPlayer._volume_before_mute = pygame.mixer.music.get_volume()
            except:
                pass
            MusicPlayer.mute()
        return MusicPlayer._is_muted
    
    @staticmethod
    def is_muted():
        """Prüfe ob Musik stummgeschaltet ist"""
        return MusicPlayer._is_muted
    
    @staticmethod
    def play_music(music_path, loops=-1, volume=0.3):
        """
        Spiele Musik ab
        
        Args:
            music_path: Pfad zur Musik-Datei
            loops: -1 = unendlich, 0 = einmal
            volume: 0.0-1.0
        """
        if not MusicPlayer._initialized:
            MusicPlayer.initialize()
        
        try:
            # Prüfe ob Datei existiert
            path = Path(music_path)
            if not path.exists():
                print(f"⚠️ Musik-Datei nicht gefunden: {music_path}")
                return False

            # Wenn bereits derselbe Track läuft, nicht neu starten
            if MusicPlayer.is_playing() and MusicPlayer._current_track == str(path):
                pygame.mixer.music.set_volume(volume)
                return True

            # Lade und spiele Musik
            pygame.mixer.music.load(str(path))
            pygame.mixer.music.set_volume(volume)
            pygame.mixer.music.play(loops)
            MusicPlayer._current_track = str(path)
            print(f"▶️ Musik gestartet: {path.name}")
            return True
            
        except Exception as e:
            print(f"Fehler beim Abspielen der Musik: {e}")
            return False
    
    @staticmethod
    def stop_music():
        """Stoppe die Musik"""
        try:
            pygame.mixer.music.stop()
            print("⏹️ Musik gestoppt")
        except Exception as e:
            print(f"Fehler beim Stoppen: {e}")
    
    @staticmethod
    def pause_music():
        """Pausiere die Musik"""
        try:
            pygame.mixer.music.pause()
            print("⏸️ Musik pausiert")
        except Exception as e:
            print(f"Fehler beim Pausieren: {e}")
    
    @staticmethod
    def unpause_music():
        """Setze die Musik fort"""
        try:
            pygame.mixer.music.unpause()
            print("▶️ Musik fortgesetzt")
        except Exception as e:
            print(f"Fehler beim Fortsetzen: {e}")
    
    @staticmethod
    def set_volume(volume):
        """Stelle die Lautstärke ein (0.0-1.0)"""
        try:
            if not MusicPlayer._is_muted:
                MusicPlayer._volume_before_mute = volume
            pygame.mixer.music.set_volume(max(0, min(1, volume)))
        except Exception as e:
            print(f"Fehler beim Einstellen der Lautstärke: {e}")
    
    @staticmethod
    def is_playing():
        """Prüfe ob Musik gerade spielt"""
        return pygame.mixer.music.get_busy()
