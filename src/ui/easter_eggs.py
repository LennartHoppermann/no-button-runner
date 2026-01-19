"""
Easter Eggs - Versteckte Features
"""

import tkinter as tk
from tkinter import messagebox
import random


class EasterEggs:
    """Verwaltung von Easter Eggs"""
    
    # Tasten-Sequenzen für Easter Eggs
    KEY_SEQUENCE = []
    KONAMI_CODE = ['<Up>', '<Up>', '<Down>', '<Down>', '<Left>', '<Right>', '<Left>', '<Right>', 'b', 'a']
    
    @staticmethod
    def setup_easter_eggs(root):
        """Setup Easter Egg Key-Bindings"""
        EasterEggs.KEY_SEQUENCE = []
        root.bind('<KeyPress>', lambda e: EasterEggs._on_keypress(e, root))
    
    @staticmethod
    def _on_keypress(event, root):
        """Verfolge Tastenfolge"""
        EasterEggs.KEY_SEQUENCE.append(event.keysym)
        
        # Behalte nur die letzten 10 Tasten
        if len(EasterEggs.KEY_SEQUENCE) > 10:
            EasterEggs.KEY_SEQUENCE.pop(0)
        
        # Prüfe auf Konami Code
        if EasterEggs.KEY_SEQUENCE[-len(EasterEggs.KONAMI_CODE):] == EasterEggs.KONAMI_CODE:
            EasterEggs._trigger_konami(root)
            EasterEggs.KEY_SEQUENCE = []
    
    @staticmethod
    def _trigger_konami(root):
        """Trigger Konami-Code Easter Egg"""
        messages = [
            "🎮 Du hast den Konami-Code gefunden! 🎮\n\nDu bist ein echter Gamer! ❤️",
            "✨ Geheime Nachricht: Ich liebe dich! ✨",
            "🎉 Du bist der beste! 🎉",
            "💘 Easter Egg gefunden! Du bist süß 💘"
        ]
        
        message = random.choice(messages)
        messagebox.showinfo("🔓 Easter Egg", message)
