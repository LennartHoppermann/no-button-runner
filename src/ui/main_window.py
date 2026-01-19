"""
Hauptfenster mit der Frage und den Ja/Nein Buttons
"""

import tkinter as tk
from tkinter import font
from src.logic.button_logic import ButtonLogic
from src.ui.restaurant_window import RestaurantWindow
from src.ui.ui_utils import HoverButton, center_window
from src.ui.confetti import ConfettiAnimation
from src.ui.easter_eggs import EasterEggs
from src.utils.audio import AudioPlayer
from src.utils.music import MusicPlayer
from src.utils.logger import logger
from src.utils.config import COLORS, WINDOW_CONFIG, CONFIG


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Valentinstag Überraschung ❤️")
        self.root.geometry(f"{WINDOW_CONFIG['width']}x{WINDOW_CONFIG['height']}")
        self.root.resizable(True, True)
        self.root.minsize(500, 400)
        self.root.config(bg=COLORS["background"])
        
        # Fenster zentrieren
        center_window(self.root, WINDOW_CONFIG["width"], WINDOW_CONFIG["height"])
        
        # Button-Logik initialisieren
        self.button_logic = ButtonLogic()
        
        # Counter Label für Nein-Button Versuche
        self.counter_label = None
        self.counter_after_id = None
        self.confetti = None
        
        # Easter Eggs Setup
        EasterEggs.setup_easter_eggs(self.root)
        
        # Starte Musik
        self._start_music()
        
        # UI erstellen
        self._create_widgets()
    
    def _start_music(self):
        """Starte die Hintergrund-Musik"""
        try:
            music_config = CONFIG.get("music", {})
            if music_config.get("enabled", False):
                music_file = music_config.get("file", "assets/music.mp3")
                volume = music_config.get("volume", 0.3)
                
                MusicPlayer.play_music(music_file, loops=-1, volume=volume)
        except Exception as e:
            print(f"Fehler beim Starten der Musik: {e}")
    
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
            command=self._on_no_clicked,
            bg_color=COLORS["danger"],
            fg_color="#ffffff"
        )
        # Wird von button_logic mit place() positioniert
        
        # Button-Logik binden
        self.button_logic.bind_button(self.no_button, self.root)
        
        # Bottom Frame für Counter
        bottom_frame = tk.Frame(self.root, bg=COLORS["background"])
        bottom_frame.pack(side=tk.BOTTOM, pady=20)
        
        # Counter Label
        counter_font = font.Font(family="Segoe UI", size=10)
        self.counter_label = tk.Label(
            bottom_frame,
            text="Versuche: 0",
            font=counter_font,
            fg=COLORS["text_light"],
            bg=COLORS["background"]
        )
        self.counter_label.pack()
        
        # Mute Button (unten rechts)
        mute_button = HoverButton(
            self.root,
            text="🔊",
            command=self._toggle_mute,
            bg_color=COLORS["primary"],
            fg_color="#ffffff"
        )
        mute_button.place(relx=0.95, rely=0.95, anchor=tk.SE, width=40, height=40)
        self.mute_button = mute_button
        
        # Update Counter Label regelmäßig
        self._update_counter()
    
    def _toggle_mute(self):
        """Toggle Musik Stummschaltung"""
        is_muted = MusicPlayer.toggle_mute()
        self.mute_button.config(text="🔇" if is_muted else "🔊")
    
    def _on_yes_clicked(self):
        """Wenn 'Ja' geklickt wird"""
        # Speichere Antwort
        logger.log_answer("Ja")
        
        # Sound + Konfetti
        AudioPlayer.play_success()
        self.confetti = ConfettiAnimation(self.root)
        self.confetti.start()
        
        # Fenster nach kurzer Zeit wechseln
        self.root.after(2000, self._switch_to_restaurant)
    
    def _on_no_clicked(self):
        """Wenn der Nein-Button doch getroffen wird"""
        from src.ui.fail_window import FailWindow
        
        # Sound abspielen (Error/Fail Sound)
        AudioPlayer.play_error()
        
        # Fenster schließen (Musik weiterlaufen lassen)
        self.root.destroy()
        
        # Fail-Fenster öffnen mit Callback zum Neustart
        fail_root = tk.Tk()
        FailWindow(fail_root, self._restart_game)
        fail_root.mainloop()
    
    def _restart_game(self):
        """Starte das Spiel neu"""
        from src.main import main
        main()
    
    def _update_counter(self):
        """Aktualisiere den Counter Label"""
        count = self.button_logic.escape_count
        
        if count == 0:
            text = "Versuche: 0"
        elif count == 1:
            text = "1 Versuch... 😏"
        elif count < 5:
            text = f"{count} Versuche... 😄"
        elif count < 10:
            text = f"{count} Versuche! Hartnäckig! 😅"
        elif count < 20:
            text = f"{count} Versuche!! Du gibst nicht auf! 💪"
        else:
            text = f"{count} VERSUCHE!!! 🤣 Ich gewinne!"
        
        self.counter_label.config(text=text)
        
        # Rufe dich selbst alle 200ms auf
        self.counter_after_id = self.root.after(200, self._update_counter)
    
    def _switch_to_restaurant(self):
        """Wechsle zur Restaurant-Seite"""
        # Stoppe alle pending callbacks und Animationen
        if self.counter_after_id:
            self.root.after_cancel(self.counter_after_id)
        if self.confetti:
            self.confetti.stop()
        
        self.root.destroy()
        new_root = tk.Tk()
        RestaurantWindow(new_root)
        new_root.mainloop()


