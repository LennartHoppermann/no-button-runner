"""
Hauptfenster mit der Frage und den Ja/Nein Buttons
"""

import tkinter as tk
from tkinter import font
from src.logic.button_logic import ButtonLogic
from src.ui.restaurant_window import RestaurantWindow
from src.ui.ui_utils import HoverButton, center_window
from src.utils.config import COLORS, WINDOW_CONFIG


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Valentinstag Überraschung ❤️")
        self.root.geometry(f"{WINDOW_CONFIG['width']}x{WINDOW_CONFIG['height']}")
        self.root.resizable(WINDOW_CONFIG["resizable"], WINDOW_CONFIG["resizable"])
        self.root.config(bg=COLORS["background"])
        
        # Fenster zentrieren
        center_window(self.root, WINDOW_CONFIG["width"], WINDOW_CONFIG["height"])
        
        # Button-Logik initialisieren
        self.button_logic = ButtonLogic()
        
        # UI erstellen
        self._create_widgets()
    
    def _create_widgets(self):
        """Erstelle die UI-Elemente"""
        # Top Frame mit schönem Abstand
        top_frame = tk.Frame(self.root, bg=COLORS["background"])
        top_frame.pack(pady=60, padx=40, expand=True)
        
        # Haupttitel - minimalistisch, elegant
        title_font = font.Font(family="Segoe UI", size=26, weight="bold")
        title_label = tk.Label(
            top_frame,
            text="Willst du mein",
            font=title_font,
            fg=COLORS["text_dark"],
            bg=COLORS["background"]
        )
        title_label.pack()
        
        # Untertitel
        subtitle_font = font.Font(family="Segoe UI", size=26, weight="bold")
        subtitle_label = tk.Label(
            top_frame,
            text="Valentinstagsschatz sein?",
            font=subtitle_font,
            fg=COLORS["primary"],
            bg=COLORS["background"]
        )
        subtitle_label.pack()
        
        # Dekorativer Text (subtil)
        deco_font = font.Font(family="Segoe UI", size=10)
        deco_label = tk.Label(
            top_frame,
            text="Eine kleine Überraschung für dich",
            font=deco_font,
            fg=COLORS["text_light"],
            bg=COLORS["background"]
        )
        deco_label.pack(pady=20)
        
        # Button-Frame
        button_frame = tk.Frame(self.root, bg=COLORS["background"])
        button_frame.pack(pady=50, expand=True)
        
        # Ja-Button - Modern, flat design
        yes_button = HoverButton(
            button_frame,
            text="Ja, gerne",
            command=self._on_yes_clicked,
            bg_color=COLORS["success"],
            fg_color="#ffffff"
        )
        yes_button.pack(side=tk.LEFT, padx=20)
        
        # Nein-Button (wird in der Logik bewegt)
        self.no_button = HoverButton(
            self.root,
            text="Nein",
            bg_color=COLORS["danger"],
            fg_color="#ffffff"
        )
        # Wird von button_logic mit place() positioniert
        
        # Button-Logik binden
        self.button_logic.bind_button(self.no_button, self.root)
    
    def _on_yes_clicked(self):
        """Wenn 'Ja' geklickt wird"""
        self.root.destroy()
        new_root = tk.Tk()
        RestaurantWindow(new_root)
        new_root.mainloop()

