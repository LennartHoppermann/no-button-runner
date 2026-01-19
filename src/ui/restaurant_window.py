"""
Restaurant-Fenster mit Details zum Abend - zwei Spalten Layout
"""

import tkinter as tk
from tkinter import font
from pathlib import Path
from PIL import Image, ImageTk
from src.utils.config import COLORS, WINDOW_CONFIG, RESTAURANT_DATA
from src.ui.ui_utils import HoverButton, center_window
from src.utils.music import MusicPlayer


class RestaurantWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Unser Abend ❤️")
        self.root.geometry("1200x700")
        self.root.resizable(True, True)
        self.root.minsize(900, 500)
        self.root.config(bg=COLORS["background"])
        self.mute_button = None  # will be created in _create_widgets
        
        # Fenster zentrieren
        center_window(self.root, 1200, 700)
        
        self.photo_image = None  # Referenz halten für Garbage Collection
        self._create_widgets()
    
    def _create_widgets(self):
        """Erstelle die UI-Elemente - zwei Spalten Layout"""
        # Main Frame mit zwei Spalten
        main_frame = tk.Frame(self.root, bg=COLORS["background"])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # ===== LINKE SPALTE - Restaurant-Info =====
        left_frame = tk.Frame(main_frame, bg=COLORS["background"])
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)
        
        # Titel
        title_font = font.Font(family="Segoe UI", size=22, weight="bold")
        title_label = tk.Label(
            left_frame,
            text="Dein ganz persönlicher Abend",
            font=title_font,
            fg=COLORS["text_dark"],
            bg=COLORS["background"]
        )
        title_label.pack(pady=10, anchor="w")
        
        # Restaurant-Informationen Frame
        info_frame = tk.Frame(left_frame, bg=COLORS["white"], relief=tk.FLAT, bd=0)
        info_frame.pack(pady=10, padx=0, fill=tk.BOTH)
        
        # Top Border
        border_top = tk.Frame(info_frame, bg=COLORS["primary"], height=3)
        border_top.pack(fill=tk.X, padx=0, pady=0)
        
        # Restaurant Name
        name_label = tk.Label(
            info_frame,
            text=RESTAURANT_DATA["name"],
            font=font.Font(family="Segoe UI", size=16, weight="bold"),
            fg=COLORS["text_dark"],
            bg=COLORS["white"]
        )
        name_label.pack(pady=12, padx=20, anchor="w")
        
        # Content Frame mit Infos
        content_frame = tk.Frame(info_frame, bg=COLORS["white"])
        content_frame.pack(fill=tk.X, padx=30, pady=10)
        
        # Adresse
        address_label = tk.Label(
            content_frame,
            text=f"📍 {RESTAURANT_DATA['address']}",
            font=font.Font(family="Segoe UI", size=10),
            fg=COLORS["text_dark"],
            bg=COLORS["white"],
            justify=tk.LEFT
        )
        address_label.pack(pady=6, anchor="w")
        
        # Uhrzeit
        time_label = tk.Label(
            content_frame,
            text=f"🕒 {RESTAURANT_DATA['time']}",
            font=font.Font(family="Segoe UI", size=10),
            fg=COLORS["text_dark"],
            bg=COLORS["white"]
        )
        time_label.pack(pady=6, anchor="w")
        
        # Notizen
        notes_label = tk.Label(
            content_frame,
            text=f"📞 {RESTAURANT_DATA['phone']}",
            font=font.Font(family="Segoe UI", size=9),
            fg=COLORS["text_light"],
            bg=COLORS["white"]
        )
        notes_label.pack(pady=6, anchor="w")
        
        # Nachricht
        message_label = tk.Label(
            left_frame,
            text="Ich freue mich auf diesen besonderen Abend mit dir",
            font=font.Font(family="Segoe UI", size=10),
            fg=COLORS["primary"],
            bg=COLORS["background"],
            wraplength=350,
            justify=tk.CENTER
        )
        message_label.pack(pady=15, expand=True)
        
        # Button Frame
        button_frame = tk.Frame(left_frame, bg=COLORS["background"])
        button_frame.pack(pady=10, fill=tk.X)
        
        # Movies Button
        movies_button = HoverButton(
            button_frame,
            text="Das war natürlich noch nicht alles 🎬",
            command=self._show_movies,
            bg_color=COLORS["primary"],
            fg_color="#ffffff"
        )
        movies_button.pack(pady=8, fill=tk.X)
        
        # Close Button
        close_button = HoverButton(
            button_frame,
            text="Bis dann!",
            command=self.root.destroy,
            bg_color=COLORS["success"],
            fg_color="#ffffff"
        )
        close_button.pack(pady=5, fill=tk.X)
        
        # ===== RECHTE SPALTE - Dante Foto =====
        right_frame = tk.Frame(main_frame, bg=COLORS["background"])
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)
        
        # Mute Button (unten rechts)
        self.mute_button = HoverButton(
            self.root,
            text="🔊" if not MusicPlayer.is_muted() else "🔇",
            command=self._toggle_mute,
            bg_color=COLORS["primary"],
            fg_color="#ffffff"
        )
        self.mute_button.place(relx=0.95, rely=0.95, anchor=tk.SE, width=40, height=40)
        
        # Chef/Koch Bild
        chef_image_path = RESTAURANT_DATA.get("chef_image")
        if chef_image_path:
            self._add_chef_image(right_frame, chef_image_path)
    
    def _add_chef_image(self, parent_frame, image_path):
        """Füge das Bild des Kochs hinzu"""
        try:
            from pathlib import Path
            
            # Verschiedene Pfade versuchen
            base_dir = Path(__file__).parent.parent.parent  # Projekt-Root
            possible_paths = [
                base_dir / image_path,
                Path(image_path),
                base_dir / "assets" / Path(image_path).name,
            ]
            
            path = None
            for p in possible_paths:
                if p.exists():
                    path = p
                    break
            
            # Fallback: in assets nach Datei mit passendem Namen und gängigen Endungen suchen
            if not path:
                assets_dir = base_dir / "assets"
                stem = Path(image_path).stem.lower()
                candidates = [
                    assets_dir / f"{stem}.png",
                    assets_dir / f"{stem}.jpg",
                    assets_dir / f"{stem}.jpeg",
                    assets_dir / f"{stem.capitalize()}.png",
                    assets_dir / f"{stem.capitalize()}.jpg",
                    assets_dir / f"{stem.capitalize()}.jpeg",
                ]
                for c in candidates:
                    if c.exists():
                        path = c
                        break

            if not path:
                print(f"Chef image not found for path: {image_path}")
                return
            
            # Lade und skaliere Bild
            image = Image.open(str(path.resolve())).convert("RGBA")
            original_size = image.size
            
            # Bild mit Aspect-Ratio-Berechnung anpassen
            # Ziel: 600 Pixel Höhe
            max_height = 600
            aspect_ratio = image.width / image.height
            new_width = int(max_height * aspect_ratio)
            new_height = max_height
            
            image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Konvertiere zu PhotoImage
            self.photo_image = ImageTk.PhotoImage(image)
            
            # Image Frame - sauberes Design
            image_frame = tk.Frame(parent_frame, bg=COLORS["white"], relief=tk.FLAT, bd=0)
            image_frame.pack(pady=20, padx=20, fill=tk.BOTH)
            
            # "Chefkoch Dante" Überschrift über dem Bild
            title_label = tk.Label(
                image_frame,
                text="Chefkoch Dante",
                font=font.Font(family="Segoe UI", size=14, weight="bold"),
                fg=COLORS["primary"],
                bg=COLORS["white"]
            )
            title_label.pack(pady=10)
            
            # Image Label - sauberes Design
            img_label = tk.Label(
                image_frame,
                image=self.photo_image,
                bg=COLORS["white"],
                relief=tk.FLAT,
                bd=0,
                width=self.photo_image.width(),
                height=self.photo_image.height()
            )
            img_label.pack(padx=10, pady=10)
            img_label.image = self.photo_image  # Zusätzliche Referenz halten
            
            # Kleines Debug-Log
            print(f"Chef image loaded: {path.name} original={original_size} resized={new_width}x{new_height}")
            
        except Exception as e:
            print(f"Error loading chef image: {e}")
    
    def _show_movies(self):
        """Zeige Film-Empfehlungen Fenster"""
        from src.ui.movies_window import MoviesWindow
        
        self.root.destroy()
        movies_root = tk.Tk()
        MoviesWindow(movies_root)
        movies_root.mainloop()
    
    def _toggle_mute(self):
        """Toggle Musik Stummschaltung"""
        is_muted = MusicPlayer.toggle_mute()
        self.mute_button.config(text="🔇" if is_muted else "🔊")
