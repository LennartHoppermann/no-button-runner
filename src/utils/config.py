"""
Konfiguration für das Valentinstags-Programm
"""

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

# ===== RESTAURANT-DATEN =====
RESTAURANT_DATA = {
    "name": "[Restaurant Name]",
    "address": "Straße 123, 12345 Stadt",
    "time": "19:00 Uhr",
    "website": "https://example.com",  # Optional
    "notes": "Reservierung unter: 0123 456789"
}

# Abstands-Schwellenwert für Button-Ausweichung (in Pixeln)
# Je kleiner die Zahl, desto näher muss die Maus ran - je größer, desto früher springt der Button
ESCAPE_DISTANCE = 120
