"""
Fenster mit animiertem Film-Karussell
"""

import tkinter as tk
from tkinter import font
import threading
import time
from src.utils.config import COLORS, WINDOW_CONFIG
from src.utils.config import CAROUSEL_CONFIG
from pathlib import Path
from PIL import Image, ImageTk
from src.ui.ui_utils import HoverButton, center_window
from src.utils.music import MusicPlayer


# Echte Filme mit Postern
MOVIES = [
    {
        "title": "WALL·E",
        "description": "Ein liebevoller Pixar-Film über einen kleinen Roboter, der die Erde aufräumt und die Liebe entdeckt.",
        "image": "assets/WALL-E.jpg",
    },
    {
        "title": "Ghostbusters II",
        "description": "Das Ghostbusters-Team ist zurück – mit Schleim, Spuk und jeder Menge Spaß in New York.",
        "image": "assets/Ghostbuster_2.jpg",
    },
    {
        "title": "Mitty",
        "description": "Das erstaunliche Leben des Walter Mitty – eine inspirierende Reise, kurz: Mitty.",
        "image": "assets/Mitty.jpg",
    },
    {
        "title": "Spider-Man: Into the Spider-Verse",
        "description": "Ein visuell beeindruckendes Multiversum-Abenteuer mit Miles Morales und vielen Spider-Helden.",
        "image": "assets/Spiderman_Into_the_Spiderverse.png",
    },
    {
        "title": "Catch the Killer",
        "description": "Ein spannender Thriller über die Jagd nach einem gefährlichen Serienmörder.",
        "image": "assets/Catch_the_killer.jpg",
    },
    {
        "title": "Fack ju Göthe",
        "description": "Eine lustige und berührende deutsche Komödie über Schule, Abenteuer und Freundschaft.",
        "image": "assets/Fack_you_Goethe.jpg",
    },
    {
        "title": "Fallout",
        "description": "Ein düsteres Post-Apokalypse-Abenteuer in einer retro-futuristischen Welt.",
        "image": "assets/Fallout.jpg",
    },
    {
        "title": "K-Pop Demon Hunters",
        "description": "Ein action-reiches Abenteuer, das K-Pop mit übernatürlichen Kämpfen vereint.",
        "image": "assets/K-Pop_Demon_Hunters.jpg",
    },
    {
        "title": "La La Land",
        "description": "Ein wundervoller Musical-Film über Träume, Musik und Liebe in Los Angeles.",
        "image": "assets/lala_land.jpg",
    },
    {
        "title": "The Terminal",
        "description": "Ein herzerwärmender Film über einen Mann, der im Flughafen-Terminal gestrandet ist.",
        "image": "assets/The_Terminal.jpg",
    },
    {
        "title": "Täglich grüßt das Murmeltier",
        "description": "Eine zeitlose Komödie über einen Moderator, der denselben Tag immer wieder erlebt.",
        "image": "assets/täglich grüßt das murmeltier.jpg",
    },
    {
        "title": "Mr. Bean macht Urlaub",
        "description": "Der legendäre Mr. Bean auf einem chaotischen Abenteuer an der französischen Riviera.",
        "image": "assets/Mr.Bean_macht_Ferien.jpg",
    },
    {
        "title": "Long Shot",
        "description": "Eine lustige romantische Komödie über eine unwahrscheinliche Liebe und politische Abenteuer.",
        "image": "assets/Long_Shot.jpg",
    },
    {
        "title": "Die Macht des Bösen",
        "description": "Ein düsterer und intensiver Thriller über Macht und Verderbtheit.",
        "image": "assets/Die_Macht_des_Bösen.webp",
    },
    {
        "title": "Besser geht's nicht",
        "description": "Eine Schwarzkomödie mit großartigem Humor und genialen Wendungen.",
        "image": "assets/Bessers geht nicht.jpg",
    },
    {
        "title": "50 erste Dates",
        "description": "Eine romantische Komödie über Liebe und zweite Chancen in Hawaii.",
        "image": "assets/50_erste_Dates.jpg",
    },
]

CARD_WIDTH = 200
CARD_HEIGHT = 280


class MoviesWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Film-Empfehlungen 🎬")
        self.root.geometry("1000x450")
        self.root.resizable(True, True)
        self.root.minsize(800, 350)
        self.root.config(bg=COLORS["background"])
        
        # Fenster zentrieren
        center_window(self.root, 1000, 450)
        
        self.selected_movie = None
        self.animation_running = True
        self.card_positions = {}
        self.current_scroll = 0
        self.mute_button = None
        
        # Bind destroy event to cleanup
        self.root.protocol("WM_DELETE_WINDOW", self._on_window_close)
        
        self._create_widgets()
        self._load_posters()
        self._start_animation()
    
    def _on_window_close(self):
        """Handle window close: stop animation and destroy"""
        self.animation_running = False
        self.root.destroy()
    
    def _create_widgets(self):
        """Erstelle die UI-Elemente"""
        # Title
        title_font = font.Font(family="Segoe UI", size=18, weight="bold")
        title_label = tk.Label(
            self.root,
            text="Welchen Film möchtest du schauen?",
            font=title_font,
            fg=COLORS["text_dark"],
            bg=COLORS["background"]
        )
        title_label.pack(pady=15)
        
        # Canvas für Karussell
        self.canvas = tk.Canvas(
            self.root,
            bg=COLORS["white"],
            relief=tk.FLAT,
            bd=0,
            height=300,
            highlightthickness=0
        )
        self.canvas.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        self.canvas.bind("<Button-1>", self._on_canvas_click)
        
        # Bottom Frame für Buttons
        bottom_frame = tk.Frame(self.root, bg=COLORS["background"])
        bottom_frame.pack(pady=20)
        
        # Mute Button (in bottom_frame aber rechts positioniert)
        button_container = tk.Frame(bottom_frame, bg=COLORS["background"])
        button_container.pack(fill=tk.X, padx=20)
        
        # Zurück Button (links)
        back_button_frame = tk.Frame(button_container, bg=COLORS["background"])
        back_button_frame.pack(side=tk.LEFT)
        # Zurück Button
        back_button = HoverButton(
            back_button_frame,
            text="Zurück",
            command=self.root.destroy,
            bg_color=COLORS["primary"],
            fg_color="#ffffff"
        )
        back_button.pack()
        
        # Mute Button (rechts)
        mute_frame = tk.Frame(button_container, bg=COLORS["background"])
        mute_frame.pack(side=tk.RIGHT)
        
        self.mute_button = HoverButton(
            mute_frame,
            text="🔊" if not MusicPlayer.is_muted() else "🔇",
            command=self._toggle_mute,
            bg_color=COLORS["primary"],
            fg_color="#ffffff"
        )
        self.mute_button.pack(side=tk.LEFT, padx=5)
    
    def _start_animation(self):
        """Starte die Animations-Loop"""
        thread = threading.Thread(target=self._animate_carousel, daemon=True)
        thread.start()

    def _resolve_image_path(self, rel_path: str) -> Path | None:
        """Finde den Poster-Pfad robust (assets, Groß/Kleinschreibung, Endungen)."""
        base_dir = Path(__file__).parent.parent.parent
        candidates = [
            base_dir / rel_path,
            base_dir / "assets" / Path(rel_path).name,
        ]
        # Fallbacks nach Endungen
        stem = Path(rel_path).stem
        for ext in (".png", ".jpg", ".jpeg"):
            candidates.append(base_dir / "assets" / f"{stem}{ext}")
        for p in candidates:
            if p.exists():
                return p
        return None

    def _load_posters(self):
        """Lade und skaliere Poster für die Karten."""
        self.tk_posters = []
        target_h = 160  # Platz für Poster im Card
        for movie in MOVIES:
            path = self._resolve_image_path(movie.get("image", ""))
            if not path:
                self.tk_posters.append(None)
                continue
            try:
                img = Image.open(str(path.resolve())).convert("RGBA")
                aspect = img.width / img.height
                new_w = int(target_h * aspect)
                img = img.resize((new_w, target_h), Image.Resampling.LANCZOS)
                tkimg = ImageTk.PhotoImage(img, master=self.root)
                self.tk_posters.append(tkimg)
            except Exception as e:
                print(f"Poster load failed for {path.name}: {e}")
                self.tk_posters.append(None)
    
    def _animate_carousel(self):
        """Animiere das Karussell"""
        while self.animation_running:
            try:
                self.current_scroll += CAROUSEL_CONFIG["scroll_speed"]
                
                self.root.after(0, self._draw_carousel)
                time.sleep(1.0 / CAROUSEL_CONFIG["fps"])
            except:
                self.animation_running = False
                break
    
    def _draw_carousel(self):
        """Zeichne die Film-Karten auf den Canvas - mit nahtlosem Loop"""
        try:
            self.canvas.delete("all")
            
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()
            
            # Berechne die gesamte Breite einer kompletten Runde
            total_width = CARD_WIDTH * len(MOVIES)
            
            # Zeichne Filme 3x hintereinander für nahtlosen Loop
            for repeat in range(3):
                for i, movie in enumerate(MOVIES):
                    x = canvas_width + (repeat * total_width) + (i * CARD_WIDTH) - self.current_scroll
                    
                    # Nur zeichnen wenn im sichtbaren Bereich
                    if -CARD_WIDTH < x < canvas_width + CARD_WIDTH:
                        self._draw_card(movie, x, i)
            
            # Nahtlos zurücksetzen wenn erste Runde vorbei ist (unsichtbar für Benutzer)
            if self.current_scroll > total_width:
                self.current_scroll = 0
        except:
            pass
    
    def _draw_card(self, movie, x, index):
        """Zeichne eine einzelne Film-Karte"""
        y = (self.canvas.winfo_height() - CARD_HEIGHT) // 2
        
        # Hintergrund
        card_id = self.canvas.create_rectangle(
            x, y,
            x + CARD_WIDTH, y + CARD_HEIGHT,
            fill=COLORS["white"],
            outline=COLORS["primary"],
            width=2,
            tags=f"card_{index}"
        )
        
        # Speichere Position für Klick-Erkennung
        self.card_positions[card_id] = index
        
        # Poster-Bild (falls vorhanden), ansonsten Platzhalter
        poster = None
        if hasattr(self, "tk_posters") and index < len(self.tk_posters):
            poster = self.tk_posters[index]
        if poster:
            self.canvas.create_image(
                x + CARD_WIDTH // 2, y + 20,
                image=poster,
                anchor="n",
                tags=f"card_{index}"
            )
        else:
            # Platzhalter-Feld wenn kein Poster
            self.canvas.create_rectangle(
                x + 20, y + 20,
                x + CARD_WIDTH - 20, y + 20 + 160,
                fill=COLORS["border"],
                outline=COLORS["primary"],
                width=1,
                tags=f"card_{index}"
            )
        
        # Titel
        title_text = self.canvas.create_text(
            x + CARD_WIDTH // 2, y + 200,
            text=movie["title"],
            font=("Segoe UI", 12, "bold"),
            width=CARD_WIDTH - 20,
            tags=f"card_{index}"
        )
        
        # Kurze Beschreibung
        desc_text = self.canvas.create_text(
            x + CARD_WIDTH // 2, y + 230,
            text="Klick für mehr…",
            font=("Segoe UI", 9, "italic"),
            fill=COLORS["text_light"],
            width=CARD_WIDTH - 20,
            tags=f"card_{index}"
        )
    
    def _on_canvas_click(self, event):
        """Fenster zum Klicken auf eine Karte"""
        try:
            # Finde Karte unter Maus
            canvas_width = self.canvas.winfo_width()
            
            # Welcher Film wurde geklickt?
            for i, movie in enumerate(MOVIES):
                x = canvas_width + (i * CARD_WIDTH) - self.current_scroll
                
                if x < event.x < x + CARD_WIDTH:
                    self._show_movie_details(i, movie)
                    break
        except:
            pass
    
    def _show_movie_details(self, index, movie):
        """Zeige Film-Details in neuem Fenster"""
        from src.ui.movie_detail_window import MovieDetailWindow
        
        detail_root = tk.Tk()
        MovieDetailWindow(detail_root, movie, index, MOVIES)
        detail_root.mainloop()
    
    def _toggle_mute(self):
        """Toggle Musik Stummschaltung"""
        is_muted = MusicPlayer.toggle_mute()
        self.mute_button.config(text="🔇" if is_muted else "🔊")


