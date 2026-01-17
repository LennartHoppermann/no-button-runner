"""
Restaurant-Fenster mit Details zum Abend
"""

import tkinter as tk
from tkinter import font
from src.utils.config import COLORS, WINDOW_CONFIG, RESTAURANT_DATA
from src.ui.ui_utils import HoverButton, center_window


class RestaurantWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Unser Abend ❤️")
        self.root.geometry(f"{WINDOW_CONFIG['width']}x{WINDOW_CONFIG['height']}")
        self.root.resizable(WINDOW_CONFIG["resizable"], WINDOW_CONFIG["resizable"])
        self.root.config(bg=COLORS["background"])
        
        # Fenster zentrieren
        center_window(self.root, WINDOW_CONFIG["width"], WINDOW_CONFIG["height"])
        
        self._create_widgets()
    
    def _create_widgets(self):
        """Erstelle die UI-Elemente"""
        # Titel
        title_font = font.Font(family="Segoe UI", size=24, weight="bold")
        title_label = tk.Label(
            self.root,
            text="Dein ganz persönlicher Abend",
            font=title_font,
            fg=COLORS["text_dark"],
            bg=COLORS["background"]
        )
        title_label.pack(pady=30)
        
        # Restaurant-Informationen Frame - sauberes, modernes Design
        info_frame = tk.Frame(self.root, bg=COLORS["white"], relief=tk.FLAT, bd=0)
        info_frame.pack(pady=20, padx=40, fill=tk.BOTH, expand=True)
        
        # Top Border (subtil)
        border_top = tk.Frame(info_frame, bg=COLORS["primary"], height=3)
        border_top.pack(fill=tk.X, padx=0, pady=0)
        
        # Restaurant Name
        name_label = tk.Label(
            info_frame,
            text=RESTAURANT_DATA["name"],
            font=font.Font(family="Segoe UI", size=18, weight="bold"),
            fg=COLORS["text_dark"],
            bg=COLORS["white"]
        )
        name_label.pack(pady=20, padx=20, anchor="w")
        
        # Content Frame mit Infos
        content_frame = tk.Frame(info_frame, bg=COLORS["white"])
        content_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=15)
        
        # Adresse
        address_label = tk.Label(
            content_frame,
            text=f"📍 {RESTAURANT_DATA['address']}",
            font=font.Font(family="Segoe UI", size=11),
            fg=COLORS["text_dark"],
            bg=COLORS["white"],
            justify=tk.LEFT
        )
        address_label.pack(pady=8, anchor="w")
        
        # Uhrzeit
        time_label = tk.Label(
            content_frame,
            text=f"🕒 {RESTAURANT_DATA['time']}",
            font=font.Font(family="Segoe UI", size=11),
            fg=COLORS["text_dark"],
            bg=COLORS["white"]
        )
        time_label.pack(pady=8, anchor="w")
        
        # Notizen
        notes_label = tk.Label(
            content_frame,
            text=f"📞 {RESTAURANT_DATA['notes']}",
            font=font.Font(family="Segoe UI", size=10),
            fg=COLORS["text_light"],
            bg=COLORS["white"]
        )
        notes_label.pack(pady=8, anchor="w")
        
        # Nachricht - elegant und dezent
        message_label = tk.Label(
            self.root,
            text="Ich freue mich auf diesen besonderen Abend mit dir",
            font=font.Font(family="Segoe UI", size=11),
            fg=COLORS["primary"],
            bg=COLORS["background"],
            wraplength=500,
            justify=tk.CENTER
        )
        message_label.pack(pady=30)
        
        # Bottom Frame für Button
        bottom_frame = tk.Frame(self.root, bg=COLORS["background"])
        bottom_frame.pack(side=tk.BOTTOM, pady=25)
        
        # Close Button - Modern und clean
        close_button = HoverButton(
            bottom_frame,
            text="Bis dann!",
            command=self.root.destroy,
            bg_color=COLORS["primary"],
            fg_color=COLORS["white"]
        )
        close_button.pack()

