"""
Detailfenster für einzelne Filme
"""

import tkinter as tk
from tkinter import font
from pathlib import Path
from PIL import Image, ImageTk
from src.utils.config import COLORS, WINDOW_CONFIG
from src.ui.ui_utils import HoverButton, center_window


class MovieDetailWindow:
    def __init__(self, root, movie, index, all_movies):
        self.root = root
        self.movie = movie
        self.index = index
        self.all_movies = all_movies
        
        self.root.title(f"{movie['title']} 🎬")
        self.root.geometry("700x500")
        self.root.resizable(True, True)
        self.root.minsize(500, 400)
        self.root.config(bg=COLORS["background"])
        
        # Fenster zentrieren
        center_window(self.root, 700, 500)
        
        self._create_widgets()
    
    def _create_widgets(self):
        """Erstelle die UI-Elemente"""
        # Main Frame
        main_frame = tk.Frame(self.root, bg=COLORS["background"])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=40, pady=30)
        
        # Poster oben anzeigen (falls vorhanden)
        poster_frame = tk.Frame(main_frame, bg=COLORS["background"])
        poster_frame.pack(pady=10)
        self._add_poster(poster_frame, self.movie.get("image", ""))
        
        # Titel
        title_font = font.Font(family="Segoe UI", size=22, weight="bold")
        title_label = tk.Label(
            main_frame,
            text=self.movie["title"],
            font=title_font,
            fg=COLORS["text_dark"],
            bg=COLORS["background"]
        )
        title_label.pack(pady=10)
        
        # Beschreibung
        desc_font = font.Font(family="Segoe UI", size=12)
        desc_label = tk.Label(
            main_frame,
            text=self.movie["description"],
            font=desc_font,
            fg=COLORS["text_dark"],
            bg=COLORS["background"],
            wraplength=600,
            justify=tk.CENTER
        )
        desc_label.pack(pady=30, expand=True)
        
        # Info Text
        info_font = font.Font(family="Segoe UI", size=10, slant="italic")
        info_label = tk.Label(
            main_frame,
            text=f"Film {self.index + 1} von {len(self.all_movies)}",
            font=info_font,
            fg=COLORS["text_light"],
            bg=COLORS["background"]
        )
        info_label.pack(pady=10)
        
        # Button Frame
        button_frame = tk.Frame(main_frame, bg=COLORS["background"])
        button_frame.pack(pady=20)
        
        # Zurück Button
        back_button = HoverButton(
            button_frame,
            text="Zurück zur Auswahl",
            command=self.root.destroy,
            bg_color=COLORS["primary"],
            fg_color="#ffffff"
        )
        back_button.pack(side=tk.LEFT, padx=10)
        
        # Navigation
        if self.index > 0:
            prev_button = HoverButton(
                button_frame,
                text="← Vorheriger",
                command=self._show_previous,
                bg_color=COLORS["text_light"],
                fg_color="#ffffff"
            )
            prev_button.pack(side=tk.LEFT, padx=5)
        
        if self.index < len(self.all_movies) - 1:
            next_button = HoverButton(
                button_frame,
                text="Nächster →",
                command=self._show_next,
                bg_color=COLORS["text_light"],
                fg_color="#ffffff"
            )
            next_button.pack(side=tk.LEFT, padx=5)

    def _resolve_image_path(self, rel_path: str) -> Path | None:
        base_dir = Path(__file__).parent.parent.parent
        candidates = [
            base_dir / rel_path,
            base_dir / "assets" / Path(rel_path).name,
        ]
        stem = Path(rel_path).stem
        for ext in (".png", ".jpg", ".jpeg"):
            candidates.append(base_dir / "assets" / f"{stem}{ext}")
        for p in candidates:
            if p.exists():
                return p
        return None

    def _add_poster(self, parent_frame, image_path: str):
        try:
            path = self._resolve_image_path(image_path)
            if not path:
                return
            img = Image.open(str(path.resolve())).convert("RGBA")
            # Zielgröße für Detailansicht
            target_h = 260
            aspect = img.width / img.height
            new_w = int(target_h * aspect)
            img = img.resize((new_w, target_h), Image.Resampling.LANCZOS)
            self.tk_poster = ImageTk.PhotoImage(img, master=self.root)
            label = tk.Label(parent_frame, image=self.tk_poster, bg=COLORS["background"])
            label.pack()
            label.image = self.tk_poster
        except Exception as e:
            print(f"Detail poster load error: {e}")
    
    def _show_previous(self):
        """Zeige vorherigen Film"""
        if self.index > 0:
            self.root.destroy()
            new_root = tk.Tk()
            MovieDetailWindow(new_root, self.all_movies[self.index - 1], self.index - 1, self.all_movies)
            new_root.mainloop()
    
    def _show_next(self):
        """Zeige nächsten Film"""
        if self.index < len(self.all_movies) - 1:
            self.root.destroy()
            new_root = tk.Tk()
            MovieDetailWindow(new_root, self.all_movies[self.index + 1], self.index + 1, self.all_movies)
            new_root.mainloop()
