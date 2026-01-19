"""
Audio-Modul für Sound-Effekte
"""

import sys
import winsound
from pathlib import Path


class AudioPlayer:
    """Einfache Klasse für System-Sounds"""
    
    @staticmethod
    def play_success():
        """Spiele Success-Sound ab"""
        try:
            # Windows System Sound
            winsound.Beep(600, 200)  # 600Hz für 200ms
            winsound.Beep(800, 200)  # 800Hz für 200ms
            winsound.Beep(1000, 300)  # 1000Hz für 300ms
        except Exception as e:
            print(f"Sound-Fehler: {e}")
    
    @staticmethod
    def play_button_escape():
        """Spiele Button-Escape Sound ab (kurz)"""
        try:
            winsound.Beep(400, 80)
        except Exception as e:
            print(f"Sound-Fehler: {e}")
    
    @staticmethod
    def play_transition():
        """Spiele Übergangs-Sound ab"""
        try:
            winsound.Beep(500, 150)
            winsound.Beep(550, 150)
        except Exception as e:
            print(f"Sound-Fehler: {e}")
    
    @staticmethod
    def play_error():
        """Spiele Error-Sound ab (für Nein-Button Treffer)"""
        try:
            winsound.Beep(300, 100)
            winsound.Beep(200, 100)
            winsound.Beep(300, 200)
        except Exception as e:
            print(f"Sound-Fehler: {e}")
