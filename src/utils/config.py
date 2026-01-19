"""
Konfiguration für das Valentinstags-Programm
"""

import json
import os
from pathlib import Path


# ===== FARBEN & DESIGN (Modernes, elegantes Schema) =====
COLORS = {
    "background": "#f8f9fa",       # Sehr helles Grau (moderner als Rosa)
    "primary": "#d63384",          # Subtiles, dunkles Pink
    "secondary": "#a0325f",        # Tiefes Burgundy
    "success": "#2d6a4f",          # Dunkelgrün für Ja
    "danger": "#a4161a",           # Tiefes Rot für Nein
    "text_dark": "#1a1a1a",        # Fast Schwarz
    "text_light": "#666666",       # Mittleres Grau
    "white": "#ffffff",
    "border": "#e0e0e0",           # Subtiler Rand
    "shadow": "#cccccc"
}

# Dark Mode Farben
COLORS_DARK = {
    "background": "#1a1a1a",
    "primary": "#ff6b9d",
    "secondary": "#ff85b3",
    "success": "#52b788",
    "danger": "#e76f51",
    "text_dark": "#f0f0f0",
    "text_light": "#b0b0b0",
    "white": "#2a2a2a",
    "border": "#333333",
    "shadow": "#000000"
}

# Button-Styling
BUTTON_STYLE = {
    "font_size": 13,
    "font_weight": "bold",
    "padding_x": 28,
    "padding_y": 11,
    "relief": "flat",              # Moderner: flat statt raised
    "bd": 0,                        # Kein Border
    "cursor": "hand2",
    "activeforeground": "#ffffff",
}

# Fenster-Konfiguration
WINDOW_CONFIG = {
    "width": 700,
    "height": 500,
    "resizable": False,
}

# Carousel-Konfiguration
CAROUSEL_CONFIG = {
    "scroll_speed": 2,      # Pixel pro Frame (erhöhen = schneller)
    "fps": 30,              # Target Frames pro Second
}

# ===== CONFIG-LOADER =====
def load_config():
    """Lade Konfiguration aus JSON"""
    config_path = Path(__file__).parent.parent.parent / "restaurant_config.json"
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Fehler beim Laden der Config: {e}")
        return get_default_config()


def get_default_config():
    """Standard-Konfiguration"""
    return {
        "restaurant": {
            "name": "[Restaurant Name]",
            "address": "Straße 123, 12345 Stadt",
            "time": "19:00 Uhr",
            "phone": "0123 456789",
            "website": "https://example.com",
            "google_maps": "https://maps.google.com"
        },
        "theme": "light",
        "language": "de"
    }


# Lade aktuelle Config
CONFIG = load_config()

# ===== RESTAURANT-DATEN =====
RESTAURANT_DATA = CONFIG.get("restaurant", get_default_config()["restaurant"])

# ===== THEME & SPRACHE =====
CURRENT_THEME = CONFIG.get("theme", "light")
CURRENT_LANGUAGE = CONFIG.get("language", "de")

# Abstands-Schwellenwert für Button-Ausweichung (in Pixeln)
ESCAPE_DISTANCE = 120

