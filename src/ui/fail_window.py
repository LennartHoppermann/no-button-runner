"""
Fenster das angezeigt wird, wenn der Nein-Button doch getroffen wird
"""

import tkinter as tk
from tkinter import font
from src.utils.config import COLORS, WINDOW_CONFIG
from src.ui.ui_utils import HoverButton, center_window


class FailWindow:
    def __init__(self, root, restart_callback):
        self.root = root
        self.restart_callback = restart_callback
        
        self.root.title("Netter Versuch! 😸")
        self.root.geometry("600x400")
        self.root.resizable(True, True)
        self.root.minsize(400, 300)
        self.root.config(bg=COLORS["background"])
        
        # Fenster zentrieren
        center_window(self.root, 600, 400)
        
        self._create_widgets()
    
    def _create_widgets(self):
        """Erstelle die UI-Elemente"""
        # Main Frame
        main_frame = tk.Frame(self.root, bg=COLORS["background"])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=40)
        
        # Titel
        title_font = font.Font(family="Segoe UI", size=20, weight="bold")
        title_label = tk.Label(
            main_frame,
            text="Tja, netter Versuch! 😸",
            font=title_font,
            fg=COLORS["danger"],
            bg=COLORS["background"]
        )
        title_label.pack(pady=30)
        
        # Message
        message_font = font.Font(family="Segoe UI", size=13)
        message_label = tk.Label(
            main_frame,
            text="Aber ein Nein akzeptiert Dante nicht! 🐱\n\nEr ist viel zu schnell für dich.\nVersuch es nochmal!",
            font=message_font,
            fg=COLORS["text_dark"],
            bg=COLORS["background"],
            justify=tk.CENTER,
            wraplength=400
        )
        message_label.pack(pady=20, expand=True)
        
        # Button Frame
        button_frame = tk.Frame(main_frame, bg=COLORS["background"])
        button_frame.pack(pady=30)
        
        # Try Again Button
        try_again_button = HoverButton(
            button_frame,
            text="Noch ein Mal!",
            command=self._on_try_again,
            bg_color=COLORS["primary"],
            fg_color="#ffffff"
        )
        try_again_button.pack()
    
    def _on_try_again(self):
        """Button 'Noch ein Mal' geklickt"""
        self.root.destroy()
        self.restart_callback()
