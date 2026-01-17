"""
UI-Utilities für schöne Button-Effekte und Styling
"""

import tkinter as tk
from src.utils.config import COLORS, BUTTON_STYLE


class HoverButton(tk.Button):
    """
    Schöner Button mit Hover-Effekten
    """
    def __init__(self, parent, text, command=None, bg_color=None, fg_color="#ffffff", **kwargs):
        self.bg_color = bg_color or COLORS["primary"]
        self.fg_color = fg_color
        self.original_bg = self.bg_color
        
        super().__init__(
            parent,
            text=text,
            command=command,
            bg=self.bg_color,
            fg=self.fg_color,
            font=("Arial", BUTTON_STYLE["font_size"], "bold"),
            padx=BUTTON_STYLE["padding_x"],
            pady=BUTTON_STYLE["padding_y"],
            relief=BUTTON_STYLE["relief"],
            bd=BUTTON_STYLE["bd"],
            cursor=BUTTON_STYLE["cursor"],
            activeforeground=BUTTON_STYLE["activeforeground"],
            activebackground=self._lighten_color(self.bg_color),
            **kwargs
        )
        
        # Hover-Effekte binden
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
    
    def _on_enter(self, event):
        """Maus betritt Button"""
        self.config(bg=self._lighten_color(self.bg_color))
    
    def _on_leave(self, event):
        """Maus verlässt Button"""
        self.config(bg=self.original_bg)
    
    @staticmethod
    def _lighten_color(color):
        """Hellt eine Farbe auf (für Hover-Effekt)"""
        # Vereinfachte Variante: RGB hex-Werte erhöhen
        if color.startswith("#"):
            color = color.lstrip("#")
            rgb = tuple(int(color[i:i+2], 16) for i in (0, 2, 4))
            lightened = tuple(min(255, int(c * 1.2)) for c in rgb)
            return f"#{lightened[0]:02x}{lightened[1]:02x}{lightened[2]:02x}"
        return color


def center_window(root, width, height):
    """
    Zentriere das Fenster auf dem Bildschirm
    """
    root.update_idletasks()
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    root.geometry(f"{width}x{height}+{x}+{y}")


def set_background_gradient(canvas, color1, color2, height):
    """
    Erstelle einen Gradient-Hintergrund (optional für später)
    """
    pass
